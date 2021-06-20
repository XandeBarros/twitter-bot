from dotenv import load_dotenv
load_dotenv()

import os
import requests, json

def fahToCel(number):
  number = number - 273.15
  return number // 1

def get_weather():
  city_name = os.getenv("CITY_ID")
  api_key = os.getenv("API_KEY_WEATHER")

  url = f"https://api.openweathermap.org/data/2.5/weather?id={city_name}&appid={api_key}"

  data = requests.get(url).json()
  dataWeather = data['weather'][0]
  dataTemp = data['main']
  dataWind = data['wind']

  mainWeather = dataWeather['main']
  description = dataWeather['description']

  temp = fahToCel(dataTemp['temp'])
  feelsLike = fahToCel(dataTemp['feels_like'])
  humidity = dataTemp['humidity']

  wind = dataWind['speed']

  result = f"Imperatriz is now {mainWeather}, {description} ;). Temperatura {temp}°, sensação térmica {feelsLike}°."
  return result
