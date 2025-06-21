import requests

API_KEY = "cf009ed0a70d15304d445e66c8ba514e"  # Replace this with your actual API key

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return None, None

        data = response.json()
        weather_desc = data['weather'][0]['description'].capitalize()
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        weather_string = f"{weather_desc}, {temp}°C"
        return weather_string, icon

    except Exception as e:
        print(f"Error in get_weather: {e}")
        return None, None




