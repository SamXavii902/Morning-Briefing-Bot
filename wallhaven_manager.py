import requests
import os
import ctypes
import random
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WALLHAVEN_API_KEY")

def set_wallhaven_wallpaper():
    themes = ["iron man", "cyberpunk", "futuristic city", "landscape", "technology"]
    query = random.choice(themes)
    
    print(f"DEBUG: Searching Wallhaven for '{query}'...")

    url = f"https://wallhaven.cc/api/v1/search?q={query}&purity=100&sorting=random&atleast=1920x1080"
    if API_KEY:
        url += f"&apikey={API_KEY}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Increased timeout to 30 seconds
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code != 200:
            return f"Wallhaven Error: {response.status_code}"
            
        data = response.json().get('data', [])
        if not data:
            return f"No wallpapers found for {query}."

        wallpaper_data = data[0]
        image_url = wallpaper_data.get('path')
        image_id = wallpaper_data.get('id')
        
        print(f"DEBUG: Downloading wallpaper ID {image_id}...")
        
        # Increased download timeout to 60 seconds
        img_response = requests.get(image_url, headers=headers, timeout=60)
        
        image_path = os.path.abspath("current_wallpaper.jpg")
        
        with open(image_path, 'wb') as handler:
            handler.write(img_response.content)

        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        
        return f"I updated your wallpaper to a {query} theme. (ID: {image_id})"

    except Exception as e:
        print(f"DEBUG Error: {e}")
        return "I could not contact the wallpaper database."