# ☀️ Morning Protocol: Personal AI Assistant

A modular Python-based automation system designed to streamline your morning transition. This project serves as a centralized hub that orchestrates high-fidelity audio briefings, desktop customization, and real-time tech intelligence synchronization.

## 🚀 Features

* **Atmospheric Initialization:** Automatically launches **Spotify**, skips to a fresh track, and begins background playback.
* **High-Fidelity Audio Briefing:** Narrates weather, system health, and tech news using high-quality AI voices.
* **Interactive News Terminal:** Fetches top tech headlines and allows users to open full articles via direct terminal commands.
* **Multi-Platform Reporting:** Sends a neatly formatted Markdown report with clickable links to a secure **Telegram** line.
* **Visual Automation:** Randomly updates the desktop wallpaper using the **Wallhaven API** based on futuristic or landscape themes.
* **System Diagnostics:** Monitors battery levels, CPU load, and memory usage for a quick morning health check.
* **Daily Inspiration:** Retrieves random motivational quotes to start the day with a positive mindset.

## 🛠️ Technologies Used

* **Language:** Python 3.8+
* **APIs:** NewsAPI, OpenWeatherMap, Wallhaven, ZenQuotes, Telegram Bot API, ElevenLabs.
* **Libraries:** Pygame (Audio), PyAutoGUI (Automation), Requests, Psutil.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SamXavii902/Morning-Briefing-Bot.git](https://github.com/SamXavii902/Morning-Briefing-Bot.git)
   cd Morning-Briefing-Bot
Set up virtual environment:

Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash

pip install -r requirements.txt
Configuration: Create a .env file in the root directory and add your API keys:

Code snippet

WEATHER_API_KEY=your_key
LOCATION=your_city
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_id
ELEVENLABS_API_KEY=your_key
🎮 Usage
Run the main protocol to begin your morning briefing:

Bash

python main.py