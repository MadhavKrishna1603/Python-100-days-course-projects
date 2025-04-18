import requests
from datetime import datetime
import smtplib
import  time

MY_LAT = 13.031744 # Your latitude
MY_LONG = 80.181671 # Your longitude

MY_EMAIL="madhavkrishnapython@gmail.com"
MY_PASSWORD="**your app password**"
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour>sunset or time_now.hour<=sunrise:
        return True
while True:
    time.sleep(60)

    if iss_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs="madhavkrishnapython@yahoo.com",msg="Subject:ISS above your head\n\nThe ISS satlite is above your head go out and look!")





