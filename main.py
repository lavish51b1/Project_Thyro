# Thyro - Main File
# Brain of the assistant - wake word detection and command routing

from features.speaker import speak
from features.listener import listen
from features.greeter import greet
from features.music import play_music, play_default, next_song, shuffle_music, pause_music, resume_music, stop_music, volume_up, volume_down
from features.websites import browse
from features.alarm import set_alarm
from datetime import datetime

def tell_time():
    now = datetime.now()
    speak(f"The current time is {now.strftime('%I:%M %p')} ")

def handle_command(command):
    if "play next" in command or "next song" in command:
        next_song()
        return

    elif "play shuffle" in command or "shuffle" in command:
        shuffle_music()
        return

    elif "play music" in command:
        play_default()
        return

    elif "play" in command:
        query = command.replace("play", "").strip()
        if not query:
            speak("Please tell me the song name!")
        else:
            play_music(query)
        return

    elif "pause" in command:
        pause_music()
        return

    elif "resume" in command:
        resume_music()
        return

    elif "stop music" in command:
        stop_music()
        return

    elif "volume up" in command:
        volume_up()
        return

    elif "volume down" in command:
        volume_down()
        return

    elif "exit" in command or "shutdown" in command:
        speak("Thyro is shutting down. Goodbye Sir, see you next time!")
        exit()

    elif "open" in command:
        browse(command)
        return

    elif "time" in command or "date" in command:
        tell_time()
        return

    elif "alarm" in command or "reminder" in command:
        speak("What time should I set the alarm for?")
        alarm_time = listen()
        alarm_time = alarm_time.replace(" ", ":")
        set_alarm(alarm_time)
        return

    else:
        speak("Sorry, I did not understand that. Please try again!")

# ── MAIN LOOP ──
print("-" * 40)
print("           THYRO is starting up...")
print("-" * 40)

greet()
speak("How Can I help you today?")

while True:

    command = listen()
    if not command:
        continue

    command = command.lower().strip()
    handle_command(command)

