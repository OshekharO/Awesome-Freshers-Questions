    import requests

    API_KEY = "YOUR_API_KEY" # Replace with your actual API key
    CITY_NAME = "London"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": CITY_NAME,
        "appid": API_KEY,
        "units": "metric" # or "imperial" or "standard"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        print(f"Current temperature in {CITY_NAME}: {temperature}°C")
        print(f"Weather description: {weather_description}")
    else:
        print(f"Error fetching weather data: {response.status_code}")
        print(response.json())
