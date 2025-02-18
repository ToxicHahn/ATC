import json
import vosk
import asyncio
import websockets

# Vosk-Modell laden
MODEL_PATH = "vosk_model/vosk-model-en-us-0.22"
model = vosk.Model(MODEL_PATH)

async def recognize(websocket, path=""):
    recognizer = vosk.KaldiRecognizer(model, 16000)
    async for message in websocket:
        if recognizer.AcceptWaveform(message):
            text = json.loads(recognizer.Result())["text"]
            await websocket.send(json.dumps({"recognized_text": text}))
        else:
            await websocket.send(json.dumps({"recognized_text": ""}))

async def main():
    async with websockets.serve(recognize, "0.0.0.0", 5000):
        print("WebSocket server is up and running on ws://0.0.0.0:5000")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
