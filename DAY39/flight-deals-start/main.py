# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from pprint import pprint
from datetime import datetime, timedelta
import time

from data_manager import DataManager
from flight_data import FlightData, find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager

SOURCE_LOCATION_CODE = 'LON'
STARTING_DATE = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

sheet_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
# flight_data = FlightData()
sheet_data = sheet_manager.get_data()
pprint(sheet_data)

# iterating through each record which consists of details of city, flight cost and price
for rec in sheet_data:
    # Updating the sheet when the iataCode in the sheet for a specific city is an empty string

    if rec["iataCode"] == '':
        rec["iataCode"] = flight_search.get_iata_code(rec["city"])
        sheet_manager.update_sheet(rec, rec["id"])

sheet_data = sheet_manager.get_data()
pprint(sheet_data)

for rec in sheet_data:
    print(f"Getting the flights info between {SOURCE_LOCATION_CODE} to {rec['city']}")
    # Getting the flights between the source and destination
    searched_flights = flight_search.get_flights_data_in_next_six_months(SOURCE_LOCATION_CODE, rec["iataCode"], STARTING_DATE, six_month_from_today)

    # Getting the cheapest flight
    cheapest_flight = find_cheapest_flight(searched_flights)
    print(f"{rec['city']}: €{cheapest_flight.price}")
    # Sending the msg notification through twilio when the price got dropped
    if cheapest_flight.price != "N/A" and cheapest_flight.price < rec["lowestPrice"]:
        print(f"Lower price flight found to {rec['city']}")

        notification_manager.send_sms(msg=f"ALERT: Price got dropped for the flight journey between "
                                          f"{cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                                          f"on {cheapest_flight.outdate} until {cheapest_flight.return_date}.")
    time.sleep(2)

