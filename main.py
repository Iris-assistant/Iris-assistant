import time
import requests
from tkinter import *
import speech_recognition as sr
import pyttsx3
import speech_text as st
import general_features as gf
import note_feature as nf
import book_feature as bf
import send_email as se

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = Tk()
window.geometry('600x650')
window.configure(background='#fcfeff')
global var
global var1

var = StringVar()
var1 = StringVar()


############################ digital_assistant ##################################
def digital_assistant(data):

    if "who are you" in data:
        listening = True
        var1.set(data)
        window.update()
        var.set("I am Iris, Your pretty intelligent assistant")
        window.update()
        st.respond("I am Iris, Your pretty intelligent assistant")

    elif "do for me" in data:
        listening = True
        var1.set(data)
        window.update()
        var.set("I am here to help you, I can write your notes and read them for you, sending emails , or even send SMS for any number your want, Also I can read a whole book just for you. and i can read any text from any image, i can give you weather,time,open google or youtube and search for what you want, Also i am pretty funny, i can tell you a joke and make you smile.")
        window.update()
        st.respond("I am here to help you, I can write your notes and read them for you, sending emails , or even send SMS for any number your want, Also I can read a whole book just for you. and i can read any text from any image, i can give you weather,time,open google or youtube and search for what you want, Also i am pretty funny, i can tell you a joke and make you smile.")

    elif "time" in data:
        listening = True
        var1.set(data)
        window.update()
        gf.get_time(var,window)

    elif 'YouTube' in data:
        listening = True
        var1.set(data)
        window.update()
        gf.open_youtube(var,window,var1)

    elif 'Google' in data:
        var1.set(data)
        window.update()
        listening = True
        gf.open_google(var,window,var1)

    elif "write note" in data:
        listening = True
        var1.set(data)
        window.update()
        nf.write_note(var,window,var1)


    elif "show note" in data:
        listening = True
        var1.set(data)
        window.update()
        nf.show_note(var,window)

    elif 'joke' in data:
        listening = True
        var1.set(data)
        window.update()
        gf.get_joke(var,window)


    elif 'book' in data:
        listening = True
        var1.set(data)
        window.update()
        bf.read_book(var,window)


    elif 'weather' in data:
        listening = True
        var1.set(data)
        window.update()
        Key = '71b466b89b734b6d8c5566794767010f'
        city_name = 'amman'
        url = f'https://api.weatherbit.io/v2.0/forecast/daily?city={city_name}&key={Key}'
        get_info_as_Json = requests.get(url).json()
        description = get_info_as_Json['data'][0]['weather']['description']
        tempreture=get_info_as_Json['data'][0]['high_temp']
        var.set(f'the weather in {city_name} is {description} and the temprature is {tempreture}C.')
        window.update()
        st.respond(f'the weather in {city_name} is {description} and the temprature is {tempreture}C.')
        return (f'the weather in {city_name} is {description} and the temprature is {tempreture}C.')



    elif 'email' in data:
        listening = True
        var1.set(data)
        window.update()
        se.send_email(var,window,var1)


    elif "stop" in data:
        listening = False
        var1.set(data)
        window.update()
        print('Listening stopped')
        return listening
    else:
        listening = True
        st.respond("Sorry! can you repeat .. ")
        data = st.listen()
        digital_assistant(data)
    return listening

############################ sendEmail ##################################
def start_ponit():

    st.respond("Good morning dear")
    var.set("Good morning dear")
    window.update()
    listening = True
    data = st.listen().lower()
    listening = digital_assistant(data)




################################# Tkinter ############################################




def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)



label2 = Label(window, textvariable = var1, font = 3, wraplength = 500, bg = '#EEA47F')
label2.config(font=("Courier", 15))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, font = 3 , wraplength = 500 , bg = '#ADD8E6')
label1.config(font=("Courier", 15))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='assistant.gif', format ='gif -index %i' % (i)) for i in range(100)]
window.title('Iris Digital Assistant')

label = Label(window, width = 620, height = 550 , bg = '#fcfeff')
label.place(y = 100)
window.after(0, update, 0)

btn1 = Button(text = 'Click To Talk',height = 2,width = 15,command =start_ponit,  bg = '#031a45' ,	fg = '#fff')
btn1.config(font=("Courier", 12))
btn1.place(x = 330 , y =540)
btn2 = Button(text = 'Good Bye',height = 2,width = 15, command = window.destroy, bg = '#031a45' , fg = '#fff')
btn2.config(font=("Courier", 12))
btn2.place(x = 110 , y =540)


window.mainloop()
