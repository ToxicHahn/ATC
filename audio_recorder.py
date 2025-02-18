import sounddevice as sd
import numpy as np
import keyboard
import requests

# Audio-Einstellungen
SAMPLE_RATE = 16000  
CHANNELS = 1  

# Vosk-Server (Falls auf anderem PC läuft, IP anpassen)
VOSK_SERVER_URL = "http://127.0.0.1:5000/recognize"

# Callback für die Audioaufnahme
def callback(indata, frames, time, status):
    if status:
        print(status)
    audio_buffer.extend(indata.copy())

# PTT & Streaming an Vosk-Server
def record_and_send():
    global audio_buffer
    audio_buffer = []

    print("🎤 Warte auf PTT (F1 gedrückt halten)...")
    keyboard.wait("f1")  # Warten, bis F1 gedrückt wird
    print("🎙️ Aufnahme startet...")

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, dtype="int16", callback=callback):
        while keyboard.is_pressed("f1"):
            pass  # Solange F1 gedrückt wird, aufnehmen
    
    print("🛑 Aufnahme gestoppt, sende an Server...")

    # Daten als RAW-Bytes umwandeln
    audio_data = np.concatenate(audio_buffer, axis=0).tobytes()
    
    # HTTP-POST an Vosk-Server
    response = requests.post(VOSK_SERVER_URL, data=audio_data, headers={"Content-Type": "audio/x-wav"})
    
    print("🛰️ Server-Antwort:", response.text)

# Loop für dauerhaftes Zuhören
while True:
    record_and_send()
