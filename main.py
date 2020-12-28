import time
import requests
from tkinter import *
import speech_recognition as sr
import pyttsx3

# import speech_text as st
import general_features as gf
import note_feature as nf
import book_feature as bf
import send_email as se


engine = pyttsx3.init('sapi5')
def respond(audioString):
    var.set(audioString)
    print(audioString)
    engine.say(audioString)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data




############################ digital_assistant ##################################
def digital_assistant(data):

    if "how are you" in data:
        listening = True
        respond("I am well")

    elif "what time is it" in data:
        listening = True
        gf.get_time()

    elif 'YouTube' in data:
        listening = True
        gf.open_youtube()

    elif 'Google' in data:
        listening = True
        gf.open_google()

    elif "write a note" in data:
        listening = True
        nf.write_note()


    elif "show note" in data:
        listening = True
        nf.show_note()

    elif 'joke' in data:
        listening = True
        gf.get_joke()


    elif 'book' in data:
        listening = True
        bf.read_book()


    elif 'weather' in data:
        listening = True
        Key = '71b466b89b734b6d8c5566794767010f'
        city_name = 'amman'
        url = f'https://api.weatherbit.io/v2.0/forecast/daily?city={city_name}&key={Key}'
        get_info_as_Json = requests.get(url).json()
        description = get_info_as_Json['data'][0]['weather']['description']
        tempreture=get_info_as_Json['data'][0]['high_temp']
        respond(f'the weather in {city_name} is {description} and the temprature is {tempreture}C.')
        return (f'the weather in {city_name} is {description} and the temprature is {tempreture}C.')



    elif 'email' in data:
        listening = True
        se.send_email()


    elif "stop" in data:
        listening = False
        print('Listening stopped')
        return listening
    else:
        listening = True
        respond("Sorry! can you repeat .. ")
        data = listen()
        digital_assistant(data)
    return listening

############################ sendEmail ##################################
def start_ponit():
    # time.sleep(2)
    respond("please pick to listen/chat")
    res = input()
    respond("Hi Aghead, what can I do for you?")
    listening = True
    data = listen()
    listening = digital_assistant(data)
    # while listening == True:
    #     if res == 'chat':
    #       data = input()
    #     else:
    #       data = st.listen()
    #     listening = digital_assistant(data)




































################################# Tkinter ############################################


window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)



label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='digital_image.gif', format ='gif -index %i' % (i)) for i in range(100)]
window.title('Iris Digital Assistant')

label = Label(window, width = 400, height = 400 , bg = '#FFF')
label.pack()
window.after(0, update, 0)

btn1 = Button(text = 'Click To Talk',height = 2,width = 20,command =start_ponit, bg = '#FFD740')
btn1.config(font=("Courier", 12))
btn1.pack(side = 'right')
btn2 = Button(text = 'Good Bye',height = 2,width = 20, command = window.destroy, bg = '#FF1744')
btn2.config(font=("Courier", 12))
btn2.pack(side = 'left')


window.mainloop()