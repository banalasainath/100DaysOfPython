import os

import requests
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

SHEET_USER_AUTH = os.environ.get('SHEET_AUTH_PWD')
today = datetime.now()
DATE = today.strftime("%d/%m/%Y")
TIME = today.strftime("%H:%M:%S")

NUTRITIONIX_EXERCISE_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_END_POINT = os.environ.get("SHEETY_ENDPOINT")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutritionix_params = {
    "query": str(input("Which exercise have you performed? "))
}

response = requests.post(url=NUTRITIONIX_EXERCISE_END_POINT, json=nutritionix_params, headers=headers)
print(response.json())
exercise_details = response.json()["exercises"]

sheety_headers = {
    "Authorization": f"Basic {SHEET_USER_AUTH}"
}

for exercise in exercise_details:
    sheety_params = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=SHEETY_END_POINT, json=sheety_params, headers=sheety_headers)
    print(response.text)

