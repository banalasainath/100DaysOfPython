import requests
import datetime
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
#
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# latitude and longitude we can get from
LATITUDE = 28.613939
LONGITUDE = 77.209023

parameters = {
    "lat": LATITUDE,
    "long": LONGITUDE
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

print(response.json())