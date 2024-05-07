import requests

openweather_url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "2329e57a9b4140c1c5f5e5dc1ca06a5d"
api_params = {
    "lat": "-1.454980",
    "lon": "-48.502270",
    "appid": api_key,
    "cnt": 4
}
response = requests.get(url=openweather_url, params=api_params)
response.raise_for_status()
weather_data = response.json()["list"]

will_rain = False
for hour_data in weather_data:
    timestamp_weather = hour_data["weather"]
    for code in timestamp_weather:
        if int(code["id"]) < 700:
            will_rain = True

if will_rain:
    print("Bring and umbrella.")

