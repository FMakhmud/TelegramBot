import requests

WEATHER_TOKEN = "88128bf4faf110cc7acd2f787a359263"


def get_weather_data(city):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}")
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        main = data['weather'][0]['main']
        temp = round(data['main']['temp'] - 273, 2)
        speed = data['wind']['speed']
        text = (f"<b>🏙City name</b>: {city}\n\n"
                f"<b>🌤Information about weather</b>: {main}\n\n"
                f"<b>🌡️Current temperature</b>: {temp}°C\n\n"
                f"<b>💨Wind speed</b>: {speed} km/h")
        return text
    return "Please enter the correct city name"
