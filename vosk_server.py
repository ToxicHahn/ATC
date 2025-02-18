import json
import queue
import sounddevice as sd
import vosk
from flask import Flask, request, jsonify

# Vosk-Modell laden
MODEL_PATH = "vosk_model/vosk-model-en-us-0.22"
model = vosk.Model(MODEL_PATH)
q = queue.Queue()

# Audio aufnehmen und in die Warteschlange legen
def callback(indata, frames, time, status):
    q.put(bytes(indata))

# Flask-Server für Kommunikation mit Lua
app = Flask(__name__)

@app.route("/recognize", methods=["POST"])
def recognize():
    recognizer = vosk.KaldiRecognizer(model, 16000)
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                text = json.loads(recognizer.Result())["text"]
                return jsonify({"recognized_text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
