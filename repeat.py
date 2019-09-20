from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather
import math
'''import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()'''

pl=[]
dates=[]
def talkToMe(audio):

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)




def myCommand():
   

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')


    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    talkToMe(command)

talkToMe('I am ready for your command')


while True:
    assistant(myCommand())
