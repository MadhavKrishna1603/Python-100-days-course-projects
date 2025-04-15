import requests
from twilio.rest import Client
account_sid = "your sid"
auth_token = "Your aut token code"
client = Client(account_sid, auth_token)
api_key = "eaa951b7f602c237ea0f6e9e47c4358c"
parameters = {"lat":25.46,
              "lon":91.36 ,
              "appid":api_key,
              "cnt":4}

response = requests.get(url ="https://api.openweathermap.org/data/2.5/forecast",params=parameters)

response.raise_for_status()
data=response.json()
id=data["list"][0]["weather"][0]["id"]
will_rain = False
for hour_data in data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:



    message = client.messages.create(
        body="Its gonna rain today take a umberlla!",
        from_="+18143055094",
        to="your verified number"
    )

    print(message.status)
