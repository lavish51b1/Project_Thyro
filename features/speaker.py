# Thyro - Speaker Module
# This module is responsible for Donna's voice

import pyttsx3
import threading

_lock = threading.Lock()

def create_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1.0)
    return engine

def speak(text):
    with _lock:  # only one speak at a time!
        engine = create_engine()
        print(f"Donna: {text}")
        engine.say(text)
        engine.runAndWait()
        engine.stop()