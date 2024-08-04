import os

import requests
from twilio.rest import Client

weather_api = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]


parameters = {
    "lat": 19.230400,
    "lon": 80.436539,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=weather_api, params=parameters)
response.raise_for_status()

weather_codes = [chunk["weather"][0]["id"] for chunk in response.json()["list"]]

for weather_id in weather_codes:
    if weather_id < 700:
        take_umbrella = True

if take_umbrella:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Take an umbrella☔ with you ",
        from_="+17207261620",
        to="+916305043064",
    )
    print(message.status)
    print(message.body)
