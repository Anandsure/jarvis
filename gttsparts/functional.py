from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather
import math
import cv2
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
        command = myCommand()

    return command


def assistant(command):
    if 'take' in command or 'picture' in command:
        camera = cv2.VideoCapture(0)
        _, image = camera.read()
        cv2.imwrite('new_snap.jpeg', image)
        talkToMe('Image saved')
    
    elif 'hello' in command or 'hi' in command:
        talkToMe('Hello!, how can i help you?')
    
    elif 'can' in command and 'do' in command:
        talkToMe('Right now, not a lot. you will build more of my features very soon!')


    

talkToMe('I am ready for your command')


while True:
    assistant(myCommand())
