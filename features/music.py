import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sys
import random
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import MUSIC_FOLDER
from features.speaker import speak

try:
    import pygame
    pygame.mixer.init()
    PYGAME_AVAILABLE = True
except Exception as e:
    PYGAME_AVAILABLE = False
    print(f"Pygame init error: {e}")

# Track current song index
current_index = [0]

def get_songs():
    songs = os.listdir(MUSIC_FOLDER)
    return [s for s in songs if s.lower().endswith('.mp3')]

def play_song(song_path, song_name):
    speak(f"Playing {song_name}")
    if PYGAME_AVAILABLE:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
    else:
        os.startfile(song_path)

def play_music(query):
    try:
        query = query.strip()

        # Just "play" alone
        if not query:
            speak("Please tell me the song name!")
            return None

        mp3_songs = get_songs()

        if not mp3_songs:
            speak("No songs found in music folder!")
            return None

        # Search by name
        for i, song in enumerate(mp3_songs):
            if all(word in song.lower() for word in query.split()):
                current_index[0] = i
                song_name = song.replace(".mp3", "").replace(".MP3", "")
                play_song(os.path.join(MUSIC_FOLDER, song), song_name)
                return song

        speak(f"Sorry, I can't find {query}")
        return None

    except FileNotFoundError:
        speak("Sorry, I could not find the music folder!")
    except PermissionError:
        speak("Sorry, I don't have permission to access the music folder!")
    except Exception as e:
        speak("Sorry, something went wrong while playing music!")
        print(f"Music Error: {e}")

def play_default():
    try:
        mp3_songs = get_songs()
        if not mp3_songs:
            speak("No songs found in music folder!")
            return
        song = mp3_songs[current_index[0]]
        song_name = song.replace(".mp3", "").replace(".MP3", "")
        play_song(os.path.join(MUSIC_FOLDER, song), song_name)
    except Exception as e:
        speak("Sorry, something went wrong!")
        print(f"Play Default Error: {e}")

def next_song():
    try:
        mp3_songs = get_songs()
        if not mp3_songs:
            speak("No songs found!")
            return
        # Loop back to first if at end
        current_index[0] = (current_index[0] + 1) % len(mp3_songs)
        song = mp3_songs[current_index[0]]
        song_name = song.replace(".mp3", "").replace(".MP3", "")
        play_song(os.path.join(MUSIC_FOLDER, song), song_name)
    except Exception as e:
        speak("Sorry, something went wrong!")
        print(f"Next Song Error: {e}")

def shuffle_music():
    try:
        mp3_songs = get_songs()
        if not mp3_songs:
            speak("No songs found in music folder!")
            return
        current_index[0] = random.randint(0, len(mp3_songs) - 1)
        song = mp3_songs[current_index[0]]
        song_name = song.replace(".mp3", "").replace(".MP3", "")
        speak(f"Shuffling!")
        play_song(os.path.join(MUSIC_FOLDER, song), song_name)
    except Exception as e:
        speak("Sorry, something went wrong while shuffling!")
        print(f"Shuffle Error: {e}")

def pause_music():
    try:
        if PYGAME_AVAILABLE:
            pygame.mixer.music.pause()
            speak("Music paused!")
    except Exception as e:
        print(f"Pause Error: {e}")

def resume_music():
    try:
        if PYGAME_AVAILABLE:
            pygame.mixer.music.unpause()
            speak("Resuming music!")
    except Exception as e:
        print(f"Resume Error: {e}")

def stop_music():
    try:
        if PYGAME_AVAILABLE:
            pygame.mixer.music.stop()
            speak("Music stopped!")
    except Exception as e:
        print(f"Stop Error: {e}")

def volume_up():
    try:
        if PYGAME_AVAILABLE:
            current = pygame.mixer.music.get_volume()
            new_vol = min(1.0, current + 0.1)
            pygame.mixer.music.set_volume(new_vol)
            speak("Volume increased!")
    except Exception as e:
        print(f"Volume Error: {e}")

def volume_down():
    try:
        if PYGAME_AVAILABLE:
            current = pygame.mixer.music.get_volume()
            new_vol = max(0.0, current - 0.1)
            pygame.mixer.music.set_volume(new_vol)
            speak("Volume decreased!")
    except Exception as e:
        print(f"Volume Error: {e}")


