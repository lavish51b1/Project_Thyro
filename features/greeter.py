# Thyro - Greet module
# greetings according to current time
from datetime import datetime
from features.speaker import speak

def greet():
    hour = datetime.now().hour

    if hour<12:
        speak("Good Morning Sir")
    elif hour<17:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Donna, your personal AI assistant")

