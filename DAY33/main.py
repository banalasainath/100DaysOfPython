import requests
import datetime
import time
import smtplib

# from requests.packages.urllib3.exceptions import InsecureRequestWarning
#
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from_mail = ""
pwd = ""


# latitude and longitude we can get from https://www.latlong.net/
MY_LATITUDE = 16.306652
MY_LONGITUDE = 80.436539


def is_iss_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # checking whether the iss position is +5 or -5 degrees w.r.t my location
    if MY_LATITUDE - 5 <= iss_latitude <= MY_LONGITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
        "tzid": "Asia/Kolkata"
    }
    # we can get the info of sunrise-sunset api from https://sunrise-sunset.org/api
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    # Splitting and getting the hour from this format: 2024-07-29T00:09:57+00:00
    # Splitting first by "T", and in the second part
    sunrise_time = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_time = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # print(f"sunrise_hour: {sunrise_time}")
    # print(f"sunset_hour: {sunset_time}")

    current_hour = datetime.datetime.now().hour

    if current_hour >= sunset_time or current_hour <= sunset_time:
        return True

while True:
    time.sleep(60)
    if is_night() and is_iss_near():
        connection = smtplib.SMTP("smtp.google.com")
        connection.starttls()
        connection.login(user=from_mail, password=pwd)
        connection.sendmail(from_addr=from_mail, to_addrs=from_mail,
                            msg="Subject:ISS_POSITION UPDATE 👆\n\nInternational space station is near to you")

