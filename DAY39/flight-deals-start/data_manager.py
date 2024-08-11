import os
from pprint import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()
AUTH_PWD = os.environ.get("SHEET_AUTH_PWD")

sheety_headers = {
    "Authorization": f"Basic {AUTH_PWD}"
}

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/a2478671416f336e7ff9028d326d001a/flightDeals/prices"

    def get_data(self):
        # This is used to get the data from the sheet
        sheet_response = requests.get(url=self.sheety_endpoint, headers=sheety_headers)
        return sheet_response.json()["prices"]

    def update_sheet(self, data, id):
        # This fn. is used to update the row in a sheet with the passed data
        params = {
            "price": data
        }
        sheet_response = requests.put(url=f"{self.sheety_endpoint}/{id}", json=params, headers=sheety_headers)
        # print(sheet_response.status_code)
