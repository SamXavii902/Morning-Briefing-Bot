
# ☀️ Morning Briefing Bot (J.A.R.V.I.S. Style Assistant)

A fully automated personal morning assistant that delivers weather, system status, tech news headlines, music ambience, and daily inspiration — with interactive voice + terminal control and Telegram delivery.

Built for reliability, zero-cost operation, and a clean UX. The assistant runs fully offline for voice (using pyttsx3) and uses no paid APIs by default.

---

## ✨ Features

- 🎙️ Voice Assistant (Offline & Free)
  - Speaks:
    - Weather summary
    - System vitals (CPU, RAM, battery)
    - Tech news headlines (headlines only — no URLs spoken)
    - Daily quote
  - Uses offline TTS via `pyttsx3` — no API keys or subscriptions required.

- 📰 Interactive Tech News
  - Fetches top tech headlines.
  - Each headline is:
    - Spoken aloud
    - Printed in the terminal with numbering
  - Interactive: enter a number to open the full article in your default browser, or enter `0` to skip.

- 📡 Telegram Delivery
  - Sends a clean, well-formatted report to a configured Telegram chat.
  - Report includes weather, system info, wallpaper status, numbered headlines with clickable links, and the quote of the day.

- 🎵 Background Ambience
  - Plays morning mood music while the voice assistant runs on top of the music.

- 🖼️ Smart Wallpaper
  - Fetches and sets a wallpaper (Wallhaven) based on themed searches for a futuristic vibe.

- 🧩 Designed for:
  - Zero cost (offline TTS, optional free news sources)
  - Privacy and reliability
  - Clean terminal + Telegram UX

---

## Project Structure

```
morning-briefing-bot/
│
├── main.py                  # Orchestrates the full morning flow
├── voice_manager.py         # Offline TTS (pyttsx3) controller
├── news_manager.py          # Tech news fetcher + interactive terminal
├── weather_manager.py       # Weather info provider (local/optional sources)
├── system_manager.py        # CPU, RAM, battery status
├── wallhaven_manager.py     # Wallpaper automation (fetch & set)
├── music_manager.py         # Background music controller (play/stop/volume)
├── telegram_manager.py      # Telegram message sender (formatted report)
│
├── requirements.txt
├── .env                     # Telegram secrets (not in repo)
└── README.md
```

---

## Prerequisites

- Python 3.8+ (3.10+ recommended)
- pip
- A desktop environment (for wallpaper setting) OR ability to run wallpaper commands on your OS
- Optional: Telegram bot token & chat ID to enable Telegram delivery

---

## Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/morning-briefing-bot.git
cd morning-briefing-bot
```

2. Create and activate a virtual environment
- macOS / Linux
```bash
python -m venv venv
source venv/bin/activate
```
- Windows (PowerShell)
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Environment variables
Create a `.env` file in the project root with the following variables (only required if you want Telegram delivery):

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

Do NOT commit `.env` to source control.

---

## Usage

Run the main script:

```bash
python main.py
```

Typical runtime flow:
1. Music starts (background ambience).
2. Assistant greets you (spoken).
3. Weather & system status are spoken.
4. Tech headlines are fetched, spoken, and printed to the terminal.
5. User can enter the headline number to open the article, or `0` to skip.
6. A quote is spoken.
7. Full report is sent to Telegram (if configured).

Example terminal output:

```
📰 TECH HEADLINES
------------------
1. Nvidia unveils next-gen AI GPUs
2. Google announces Gemini update
3. Microsoft integrates Copilot deeper into Windows

Enter headline number to open (0 to skip):
```

Example Telegram message (markdown):

```
☀️ Morning Briefing Protocol
------------------------------
📅 2026-01-07

🌍 Weather: Clear skies, 24°C
🔋 System: Battery 82%, CPU normal
🖼️ Visuals: Futuristic wallpaper applied

📰 Tech Headlines
1. Nvidia unveils next-gen AI GPUs
2. Google announces Gemini update
3. Microsoft integrates Copilot deeper into Windows

💬 Quote: "Discipline is the bridge between goals and accomplishment."
```

---

## Configuration & Customization

- Voice / TTS
  - `voice_manager.py` uses `pyttsx3`. You can change voice, rate, and volume in that module.
- News sources
  - `news_manager.py` can be wired to any news source. The current design fetches headlines only (no URLs are read aloud).
- Wallpaper
  - `wallhaven_manager.py` searches Wallhaven for theme-based wallpapers. Configure search terms and size preference there.
- Music
  - `music_manager.py` handles playing tracks (local or streaming). Ensure your system sound is configured to allow overlapping playback with TTS.
- Telegram
  - `telegram_manager.py` formats and sends a markdown message to the chat configured in `.env`.

---

## Security & Privacy

- No third-party TTS APIs are required — voice runs offline.
- If you add any API keys (e.g., for weather or news), place them in `.env` and do not commit that file.
- Only headlines are read aloud by default; URLs are shown in the terminal and included in Telegram messages.

---

## Troubleshooting

- No sound from TTS:
  - Ensure your system audio is functional and `pyttsx3` is installed correctly. On Linux, you may need `espeak` or `espeak-ng` and `pulseaudio` configured.
- Wallpaper not setting:
  - Wallpaper commands differ by OS. Check `wallhaven_manager.py` for OS-specific implementation and adjust commands as needed.
- Telegram message not sent:
  - Verify `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` in `.env`. Check for bot permissions and that the bot was added to the chat.
- Headlines failing to fetch:
  - If using a news site scrape, site layout changes can break parsing. Switch to a different source or update the parser in `news_manager.py`.

---

## Development Notes

- Keep the voice separate from music playback: start music in a non-blocking thread/process and route TTS audio to the default output so the voice plays over the music.
- Make the news interaction robust: timeouts and retries for fetching headlines; polite rate limiting for scrapes.
- Consider optional caching for wallpapers and headlines to reduce network calls.

---

## Dependencies

See `requirements.txt` for a full list. Typical dependencies include:
- pyttsx3 (offline TTS)
- python-dotenv (for .env)
- requests (HTTP)
- psutil (system stats)
- python-telegram-bot (or requests for a lightweight sender)
- simpleaudio / pygame / other audio libs for background music

---

## Contributing

Contributions, issues and feature requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

```
MIT License
Copyright (c) 2026 Uppu Vamsi
```

---

Thank you for using Morning Briefing Bot — your personal zero-cost, privacy-minded, voice-enabled assistant to start the day.
````
