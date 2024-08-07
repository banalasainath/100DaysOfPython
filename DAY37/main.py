import requests
from datetime import datetime
import os

# Need to pass username and token as environment variables
USER = os.environ["PIXELA_USERNAME"]
TOKEN = os.environ["PIXELA_TOKEN"]
GRAPH_ID = "tracker1"

# formatting the date according to the requirement
# today = datetime(year=2024, month=8, day=5)
today = datetime.now()
TODAY = today.strftime("%Y%m%d")


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER}/graphs"
PIXEL_ADDITION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}"
PIXEL_UPDATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}/{TODAY}"
PIXEL_DELETION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER}/graphs/{GRAPH_ID}/{TODAY}"

# creating a user
user_params = {
    "token": TOKEN,
    "username": USER,
    "notMinor": "yes",
    "agreeTermsOfService": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Creating a graph page
graph_params = {
    "id": GRAPH_ID,
    "name": "coding",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
}

# headers are the kind of metadata, which won't be directly part of an url which we send as request
headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(graph_response.text)

# graph url will be "https://pixe.la/v1/users/<user_name>/graphs/<id>.html

# Adding the effort
pixel_add_params = {
    # python strftime() used to obtain the desired date format: https://www.geeksforgeeks.org/python-strftime-function/
    "date": TODAY,
    "quantity": input(f"How much time have you spent in coding(in mins) on {TODAY}? ")
}

add_params_response = requests.post(url=PIXEL_ADDITION_ENDPOINT, json=pixel_add_params, headers=headers)
print(add_params_response.text)

# Updating already added effort
pixel_update_params = {
    "quantity": "40"
}

# response = requests.put(url=PIXEL_UPDATION_ENDPOINT, json=pixel_update_params, headers=headers)
# print(response.text)

# deleting a pixel already addeed
# response = requests.delete(url=PIXEL_DELETION_ENDPOINT, headers=headers)
