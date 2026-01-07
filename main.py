import time
import webbrowser
from datetime import datetime
from plyer import notification

# Core Managers
from voice_manager import speak
from weather_manager import get_weather
from quote_manager import get_quote
from system_manager import get_vitals_report
from wallhaven_manager import set_wallhaven_wallpaper
from news_manager import get_tech_news
from music_manager import play_morning_mood
from telegram_manager import send_telegram_report


def handle_interactive_news(news_list):
    """
    Speaks headlines only.
    Displays numbered headlines in terminal.
    Allows user to open a selected headline.
    Returns Telegram-formatted news block.
    """
    if not news_list:
        speak("There are no major tech headlines today.")
        return "📰 *Tech Headlines:* None available today."

    print("\n📰 TECH HEADLINES")
    print("------------------")

    telegram_block = "*📰 Tech Headlines*\n"

    for idx, article in enumerate(news_list, start=1):
        title = article["title"]
        url = article["url"]

        # Speak ONLY the headline
        speak(title)

        # Print headline with numbering
        print(f"{idx}. {title}")

        # Telegram formatted line
        telegram_block += f"{idx}. [{title}]({url})\n"

    # User interaction
    try:
        choice = int(input("\nEnter headline number to open (0 to skip): "))
        if choice != 0 and 1 <= choice <= len(news_list):
            webbrowser.open(news_list[choice - 1]["url"])
    except ValueError:
        print("Invalid input. Skipping headline opening.")

    return telegram_block


def main():
    print("--- INITIATING MORNING PROTOCOL ---")

    # 1. GATHER DATA (Silent Phase)
    weather_info = get_weather()
    system_info = get_vitals_report()
    wallpaper_status = set_wallhaven_wallpaper()
    tech_news = get_tech_news()
    daily_quote = get_quote()

    user_name = "Sam"

    # 2. START BACKGROUND MUSIC
    play_morning_mood(weather_info)

    # 3. SPEAK CORE BRIEFING (NO NEWS HERE)
    speak(
        f"Good morning, {user_name}. "
        f"{weather_info}. "
        f"{system_info}. "
        f"{wallpaper_status}."
    )

    # 4. HANDLE NEWS (INTERACTIVE + AUDIO)
    news_block = handle_interactive_news(tech_news)

    # 5. FINAL QUOTE
    speak(f"Here is your thought for the day. {daily_quote}")

    # 6. TELEGRAM REPORT
    telegram_text = (
        f"☀️ *Morning Briefing Protocol*\n"
        f"------------------------------\n"
        f"📅 *{datetime.now().strftime('%Y-%m-%d')}*\n\n"
        f"🌍 *Weather:* {weather_info}\n"
        f"🔋 *System:* {system_info}\n"
        f"🖼️ *Visuals:* {wallpaper_status}\n\n"
        f"{news_block}\n"
        f"💬 *Quote:* _{daily_quote}_"
    )

    send_telegram_report(telegram_text)

    # 7. SYSTEM NOTIFICATION
    notification.notify(
        title="Morning Protocol Active",
        message="Check Telegram for full briefing.",
        app_name="J.A.R.V.I.S.",
        timeout=5
    )


if __name__ == "__main__":
    main()
