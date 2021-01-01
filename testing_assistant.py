import speech_recognition as sr
from time import ctime
import time
import pyttsx3
import webbrowser
import pyjokes
import datetime
import PyPDF2
from tkinter.filedialog import *
import requests
engine = pyttsx3.init('sapi5')

def digital_assistant(data):
    if "how are you" in data:
        return "I am well"
    elif "what time is it" in data:
        time = ctime()
        return time
    elif 'YouTube' in data:
        return "Here you go to Youtube\n"
    elif 'Google' in data:
        return "Here you go to Google\n"
    elif "write a note" in data:
        file = open('iris.txt', 'w')
        file.write('hello')
        file.close()
    elif "show note" in data:
        return 'hello'
    elif "stop" in data:
        return 'Listening stopped'
    else:
        return "Sorry! can you repeat .. "















