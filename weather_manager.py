import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("LOCATION")

def get_weather():
    # --- TEMPORARY MOCK MODE (While waiting for API Key) ---
    # return f"Current weather in {CITY}: 25°C with clear sky (MOCK DATA)."
    # -------------------------------------------------------

    # Real code below (Keep this here for later!)
    if not API_KEY:
        return "Error: API Key missing."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        
        # If the key is still failing, we return mock data automatically
        if response.status_code == 401:
            return f"Current weather in {CITY}: 25°C with clear sky (Waiting for API Key activation...)"

        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"Current weather in {CITY}: {temp}°C with {desc}."
        else:
            return "Could not fetch weather data."
            
    except Exception as e:
        return f"Connection Error: {e}"