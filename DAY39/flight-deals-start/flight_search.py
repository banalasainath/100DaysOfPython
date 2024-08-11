import os
from dotenv import load_dotenv
import json
import requests
from datetime import datetime

load_dotenv()

AMADEUS_END_POINT = "https://test.api.amadeus.com"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        # generates a new token everytime
        self._token = self.get_token()
        pass

    def get_token(self):
        # Generates a authentication token used by amadeus api which will expire within 30 mins
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        token_response = requests.post(url=f"{AMADEUS_END_POINT}/v1/security/oauth2/token", data=params, headers=headers)
        return token_response.json()["access_token"]

    # Get the IATA code for a specific city by calling one of the amadeus endpoints
    def get_iata_code(self, city_name):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        params = {
            "keyword": city_name,
            "include": "AIRPORTS",
            "max": "2"
        }
        try:
            response = requests.get(url=f"{AMADEUS_END_POINT}/v1/reference-data/locations/cities", params=params, headers=headers)
            IataCode = response.json()["data"][0]["iataCode"]
        except KeyError:
            print(f"KEYERROR: No Airport code Found for city: {city_name}")
        except IndexError:
            print(f"IndexError: No Airport code found for city: {city_name}")
        return IataCode

    def get_flights_data_in_next_six_months(self, src_location_code, dest_location_code, starting_time, return_time):
        # getting the flights between src and dest
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        params = {
            "originLocationCode": src_location_code,
            "destinationLocationCode": dest_location_code,
            "departureDate": starting_time.strftime("%Y-%m-%d"),
            "returnDate": return_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
        }
        response = requests.get(url=f"{AMADEUS_END_POINT}/v2/shopping/flight-offers", params=params, headers=headers)

        return response.json()
