import pyttsx3

# Initialize once (VERY IMPORTANT for performance)
_engine = pyttsx3.init()

# Optional tuning (recommended)
_engine.setProperty("rate", 175)     # Speech speed
_engine.setProperty("volume", 1.0)   # Max volume

def speak(text: str):
    """
    Clean, offline, zero-noise text-to-speech.
    No APIs. No popups. No errors.
    """
    try:
        _engine.say(text)
        _engine.runAndWait()
    except Exception:
        pass  # Absolute silence on failure (no terminal spam)
