import requests
from urllib.parse import quote_plus
import environ

# Initialize environment variables
env = environ.Env()

def get_weather_data(city_name):
    api_key = env('WEATHER_API')  
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    city_name_encoded = quote_plus(city_name)  
    complete_url = f"{base_url}q={city_name_encoded}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200: 
        return response.json()
    else:
        return {"error": f"Unable to fetch data. Status code: {response.status_code}"}

# Usage:
weather_data = get_weather_data("Nairobi,KE")
print(weather_data)

