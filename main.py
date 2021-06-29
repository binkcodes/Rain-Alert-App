import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "redacted"
account_sid = "redacted"
auth_token = "redacted"

weather_params = {
    "lat": 29.760427,
    "lon": -95.369804,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if 700 > int(condition_code):
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today - bring an umbrella!",
            from_="redacted",
            to="redacted"
        )
    print(message.status)


#Python Anywhere Code w/ environment variables

# import requests
# import os
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
#
# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = os.environ.get("OWM_API_KEY")
# account_sid = ""
# auth_token = os.environ.get("AUTH_TOKEN")
#
# weather_params = {
#     "lat": 29.760427,
#     "lon": -95.369804,
#     "appid": api_key,
#     "exclude": "current,minutely,daily"
# }
#
# response = requests.get(OWM_Endpoint, params=weather_params)
# response.raise_for_status()
# weather_data = response.json()
# weather_slice = weather_data["hourly"][:12]
#
# will_rain = False
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if 700 > int(condition_code):
#         will_rain = True
#
# if will_rain:
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#     client = Client(account_sid, auth_token, http_client=proxy_client)
#     message = client.messages \
#         .create(
#             body="It's going to rain today - bring an umbrella!",
#             from_="",
#             to=""
#         )
#     print(message.status)
