mkdir vosk_model
cd vosk_model
Invoke-WebRequest -Uri "https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip" -OutFile "vosk-model-en-us-0.22.zip"
Invoke-WebRequest -Uri "https://alphacephei.com/vosk/models/vosk-model-de-0.21.zip" -OutFile "vosk-model-de-0.21.zip"
Expand-Archive -Path "vosk-model-en-us-0.22.zip" -DestinationPath .
Expand-Archive -Path "vosk-model-de-0.21.zip" -DestinationPath .