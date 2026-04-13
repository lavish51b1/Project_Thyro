import webbrowser
from config import WEBSITES
from features.speaker import speak

def browse(query):
    query = query.replace("open","").strip()
    if query in WEBSITES:
        speak(f"opening {query}")
        webbrowser.open(WEBSITES[query])
    else:
        speak(f"Sorry, I can't find {query}")
    return None
