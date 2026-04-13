# Thyro - AI Voice Assistant 🎙️

Hey! This is my first AI project — a voice assistant built in Python that I named **Thyro**. The voice is called **Donna** , yeah from the **Suits** 😄

Still improving it but Version 1 is working!

---

## What it does

- 🎵 Plays music from your PC — just say the song name
- 🌐 Opens websites like YouTube, Google, WhatsApp by voice
- ⏰ Sets alarms and reminders
- 🕐 Tells current time and date
- 👋 Greets you based on time of day (morning/afternoon/evening)
- 🔀 Shuffle, next song, pause, resume, volume control — all by voice

---

## Tech used

- Python 3.10.11
- pyttsx3 — for Donna's voice
- SpeechRecognition — to understand what I say
- sounddevice + scipy — for mic recording
- pygame — music playback
- webbrowser — opens websites
- threading — so alarms run in background

---

## Project structure

    AI_ROBO/
    ├── features/
    │   ├── __init__.py
    │   ├── speaker.py      
    │   ├── listener.py     
    │   ├── greeter.py      
    │   ├── music.py        
    │   ├── websites.py     
    │   └── alarm.py        
    ├── music/              
    ├── data/               
    ├── config.py           
    └── main.py             

---

## How to run it

1. Clone the repo

        git clone https://github.com/yourusername/Thyro.git
        cd Thyro

2. Create virtual environment

        python -m venv venv
        venv\Scripts\activate

3. Install the libraries

        pip install pyttsx3 SpeechRecognition sounddevice scipy pygame pywin32 comtypes

4. Add your mp3 songs inside the `music/` folder

5. Run

        python main.py

---

## Important notes

- Needs internet for voice recognition
- Works on Windows (tested on Windows 11)
- Speaks and understands English.
- Say the command clearly for better results

---

## What's coming next

- Wake word system (Hey Donna)
- **ChatGPT integration for smart replies**
- Control laptop volume and brightness
- some fun features..

This is just V1 — planning to keep building this for a long time 🚀

---

Made by **Lavish**  
