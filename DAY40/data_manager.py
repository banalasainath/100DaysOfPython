import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pprint import pprint

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        # Destination and customer details intializing
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.prices_endpoint, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, auth=self._authorization)
        data = response.json()
        # pprint(data)
        # Name of the spreadsheet 'tab' with the customer emails should be 'users'.
        self.customer_data = data["users"]
        return self.customer_data
