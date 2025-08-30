import pyttsx3
import sounddevice as sd
import numpy as np
import whisper
import requests

# ===========================
# Text-to-Speech
# ===========================
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ===========================
# Speech-to-Text (Whisper)
# ===========================
model = whisper.load_model("base")  # "small", "medium", "large" also possible

def record_audio(duration=5, fs=44100):
    print("🎤 Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return recording.flatten()

def transcribe(audio):
    audio_float = audio.astype(np.float32)
    result = model.transcribe(audio_float, fp16=False, language="en")
    return result["text"]

# ===========================
# Ollama query (HTTP API)
# ===========================
CONFIG = {"OLLAMA_MODEL": "llama2"}  # Change if you have a different local model

def query_ollama(prompt, timeout=10):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": CONFIG["OLLAMA_MODEL"],
                "prompt": prompt,
                "stream": False
            },
            timeout=timeout
        )
        return response.json()["response"].strip()
    except Exception as e:
        print(f"Ollama error: {e}")
        return "I encountered an error."

# ===========================
# Main loop
# ===========================
while True:
    audio_data = record_audio(duration=5)
    command = transcribe(audio_data).lower()
    print("You:", command)

    if "stop" in command or "exit" in command:
        speak("Goodbye!")
        break

    if command.strip():
        response = query_ollama(command)
        print("AI:", response)
        speak(response)
