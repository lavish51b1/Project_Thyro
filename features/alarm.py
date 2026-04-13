# Thyro - Alarm Module
# Sets alarms and reminders using background threading

import threading
import time
from datetime import datetime
from features.speaker import speak


def set_alarm(alarm_time_str):
    try:
        # Clean the input
        alarm_time_str = alarm_time_str.strip()

        # If no colon, try to add it
        if ":" not in alarm_time_str:
            # Remove all spaces
            alarm_time_str = alarm_time_str.replace(" ", "")
            # If 3 or 4 digits like "530" or "1512"
            if len(alarm_time_str) == 3:
                alarm_time_str = alarm_time_str[0] + ":" + alarm_time_str[1:]
            elif len(alarm_time_str) == 4:
                alarm_time_str = alarm_time_str[:2] + ":" + alarm_time_str[2:]

        alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
        now = datetime.now()
        alarm_time = alarm_time.replace(year=now.year, month=now.month, day=now.day)
        delay = (alarm_time - now).total_seconds()

        if delay < 0:
            speak("That time has already passed today!")
            return

        speak(f"Alarm set for {alarm_time_str}")

        def ring():
            time.sleep(delay)
            speak(f"Wake up sir! It is {alarm_time_str}. Your alarm is ringing!\n" * 5)

        t = threading.Thread(target=ring)
        t.daemon = True
        t.start()

    except ValueError:
        speak("Sorry, I could not understand the time.")