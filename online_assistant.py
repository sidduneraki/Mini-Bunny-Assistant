import speech_recognition as sr
import pyttsx3
import openai

say = pyttsx3.init()
s = sr.Recognizer()
openai.api_key = "API_KEY"

def listen():
    with sr.Microphone() as source:
        print("Say something...")
        audio = s.listen(source)
    try:
        text = s.recognize_google(audio)
        return text
    except:
        return ""

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def speak(text):
    say.say(text)
    say.runAndWait()

while True:
    command = listen()
    if command.lower() in ["exit", "quit", "stop"]:
        speak("Goodbye!")
        break
    if command:
        reply = ask_gpt(command)
        print("Bunny:", reply)
        speak(reply)
