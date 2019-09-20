from gtts import gTTS
import speech_recognition as sr
import os

def talkToMe(audio):

    print(audio)
    for line in audio.splitlines():
        engine = pyttsx3.init()
        engine.say("say"+ audio)
        engine.runAndWait()
        os.system("say " + audio)

def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening..')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()

        return command