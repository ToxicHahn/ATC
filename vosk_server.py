import json
import vosk
import sounddevice as sd
from flask import Flask, request, jsonify

# Vosk-Modell laden
MODEL_PATH = "vosk_model/vosk-model-en-us-0.22"
model = vosk.Model(MODEL_PATH)

# Flask-Server für Kommunikation mit Lua
app = Flask(__name__)

@app.route("/recognize", methods=["POST"])
def recognize():
    recognizer = vosk.KaldiRecognizer(model, 16000)
    
    # Empfange Audiostream
    audio_data = request.data  # Nimmt die Audio-Bytes vom Client
    if not audio_data:
        return jsonify({"error": "Kein Audio empfangen"}), 400
    
    # Audio verarbeiten
    if recognizer.AcceptWaveform(audio_data):
        text = json.loads(recognizer.Result())["text"]
        return jsonify({"recognized_text": text})
    else:
        return jsonify({"recognized_text": ""})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
