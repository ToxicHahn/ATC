import sounddevice as sd
import numpy as np
import keyboard
import asyncio
import websockets

# Audio-Einstellungen
SAMPLE_RATE = 16000  
CHANNELS = 1  

# Vosk-Server (Falls auf anderem PC läuft, IP anpassen)
VOSK_SERVER_URL = "ws://127.0.0.1:5000"

# Callback für die Audioaufnahme
def callback(indata, frames, time, status):
    if status:
        print(status)
    audio_buffer.extend(indata.copy())

# Funktion zur Audioaufnahme
def record_audio():
    global audio_buffer
    audio_buffer = []

    print("🎤 Warte auf PTT (F1 gedrückt halten)...")
    keyboard.wait("f1")  # Warten, bis F1 gedrückt wird
    print("🎙️ Aufnahme startet...")

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, dtype="int16", callback=callback):
        while keyboard.is_pressed("f1"):
            pass  # Solange F1 gedrückt wird, aufnehmen
    
    print("🛑 Aufnahme gestoppt.")
    return np.concatenate(audio_buffer, axis=0).tobytes()

# Funktion zum Senden der Audio-Daten an den Server
async def send_audio(audio_data):
    async with websockets.connect(VOSK_SERVER_URL) as websocket:
        await websocket.send(audio_data)
        return await websocket.recv()
        

# Loop für dauerhaftes Zuhören
while True:
    audio_data = record_audio()
    asyncio.run(print(send_audio(audio_data)))
