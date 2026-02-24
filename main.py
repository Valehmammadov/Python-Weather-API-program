import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

url = "https://api.weatherapi.com/v1/current.json"

params = {
    "key": API_KEY,
    "q": "Baku",
    "aqi": "no"
}

response = requests.get(url, params=params)
data = response.json()

print(data["location"]["name"])
print(data["current"]["temp_c"])
print(data["current"]["condition"]["text"])