import requests

# Example location: Berlin
latitude = 52.52
longitude = 13.41

# Open-Meteo API endpoint for current weather
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

# Fetch the weather data
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    current_weather = data['current_weather']
    temperature = current_weather['temperature']
    windspeed = current_weather['windspeed']
    weather_code = current_weather['weathercode']
    
    print(f"Current weather in Berlin:")
    print(f"Temperature: {temperature}°C")
    print(f"Wind Speed: {windspeed} km/h")
    print(f"Weather Code: {weather_code}")
else:
    print("Failed to fetch weather data.")
