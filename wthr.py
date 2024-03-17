import os
import requests
import sys
import secrets

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        print(f"\n\033[1m{city}\033[0m:\n  Temperature: {temp}°F\n  Description: {weather_description}")
    else:
        print("Error fetching weather data")

if __name__ == "__main__":
    if not secrets.api_key:
        print("Key not found")
        sys.exit(1)

    if len(sys.argv) > 1:
        city = ' '.join(sys.argv[1:])
    else:
        city = input("Enter the city name: ")
    get_weather(secrets.api_key, city)
