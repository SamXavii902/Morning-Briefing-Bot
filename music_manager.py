import pyautogui
import time
import os
import subprocess

def play_morning_mood(*args):
    try:
        # 1. Ensure Spotify is the active media focus
        print("⏭️ Skipping to next track...")
        pyautogui.press('nexttrack')
        
        # 2. INCREASE DELAY: Give Spotify more time to load the new track
        time.sleep(1.5) 
        
        # 3. Explicitly play (if already playing, this might pause, 
        # but in 'Morning Protocol' it usually starts the audio)
        print("▶️ Resuming Spotify Background Music...")
        # pyautogui.press('playpause')
        
        return True
    except Exception as e:
        print(f"❌ Music Manager Error: {e}")
        return False