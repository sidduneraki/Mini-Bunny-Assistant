# Mini-Bunny-Assistant
#Online Jarvis Assistant
🎤 Voice Assistant with OpenAI
___________________________________
This is a simple voice-controlled AI assistant built with:

speech_recognition (to listen to your voice)

pyttsx3 (to speak back)

OpenAI GPT (ChatGPT API) (to generate responses)

The assistant listens to your speech, sends it to GPT, and replies back using text-to-speech.

⚡ Features
_____________
🎙️ Voice input using microphone

🤖 AI-powered responses via GPT-3.5

🗣️ Text-to-Speech output

🚪 Exit the program by saying "exit", "quit", or "stop"

📦 Installation

Clone this repository
__________________________

git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant


Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies
___________________________

pip install speechrecognition pyttsx3 openai pyaudio


⚠️ If you face issues with pyaudio on Windows:
Download the .whl file from PyAudio Releases
 and install manually:

pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl


Set your OpenAI API key

Open the Python file and replace:

openai.api_key = "API_KEY"


with your real API key.

Or use environment variable:

export OPENAI_API_KEY="your_api_key"   # Linux/Mac
setx OPENAI_API_KEY "your_api_key"     # Windows

🚀 Usage

Run the program:

python main.py


Speak into the microphone when prompted.

The assistant will listen, generate a response, and speak it out loud.

Say "exit", "quit", or "stop" to end the program.

#for offline_mini_assistant
# Offline AI Assistant

## Features
- Offline speech-to-text using Whisper
- Offline text-to-speech using pyttsx3
- Offline AI responses using Ollama local model

## Requirements
- Python 3.10+
- Packages:

- Ollama local model installed and `ollama serve` running

## Usage
1. Run the Ollama server:
2. Run the assistant:
3. Say your commands and it will respond via voice.
