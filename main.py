import requests

openweather_url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "2329e57a9b4140c1c5f5e5dc1ca06a5d"
api_params = {
    "lat": "25.204849",
    "lon": "55.270782",
    "appid": api_key
}
r = requests.get(url=openweather_url, params=api_params)
r.raise_for_status()
print(r.json()['list'])
