# Thyro - Listener Module
# This module is responsible for listening to your voice

import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import os

def listen():
    print("Listening...")
    duration = 5
    sample_rate = 44100

    # Record audio
    recording = sd.rec(int(duration * sample_rate),
                      samplerate=sample_rate,
                      channels=1,
                      dtype='int16')
    sd.wait()

    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False).name
    wav.write(temp_file, sample_rate, recording)

    # Recognize
    r = sr.Recognizer()
    with sr.AudioFile(temp_file) as source:
        audio = r.record(source)

    os.remove(temp_file)

    try:
        command = r.recognize_google(audio, language="en-IN")
        print(f"\nYou said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""
