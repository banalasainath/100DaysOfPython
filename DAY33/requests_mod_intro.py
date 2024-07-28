import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# If the https_return code is not equal to 200, Raises exception for that specific https_return_code
response.raise_for_status()

print(response.status_code)

data = response.json()
iss_longitude = data["iss_position"]["longitude"]
iss_latitude = data["iss_position"]["latitude"]

iss_location = (iss_longitude, iss_latitude)
print(iss_location)
