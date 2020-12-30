import requests
from tkinter import *
import pyttsx3
import speech_text as st
import general_features as gf
import note_feature as nf
import book_feature as bf
import send_email as se
import sms_feature as sf
import azure_api as azure_a
import threading

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

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
        var1.set(data)
        window.update()
        var.set("I am Iris, Your pretty intelligent assistant")
        window.update()
        st.respond("I am Iris, Your pretty intelligent assistant")
    elif 'good morning' in data:
        var1.set(data)
        window.update()
        var.set("Good morning dear")
        st.respond("Good morning dear")
        window.update()

    elif "time" in data:
        var1.set(data)
        window.update()
        gf.get_time(var,window)

    elif 'youtube' in data:
        var1.set(data)
        window.update()
        gf.open_youtube(var,window,var1)

    elif 'google' in data:
        var1.set(data)
        window.update()
        gf.open_google(var,window,var1)

    elif "write" in data:
        var1.set(data)
        window.update()
        nf.write_note(var,window,var1)


    elif "show" in data:
        var1.set(data)
        window.update()
        nf.show_note(var,window)

    elif 'joke' in data:
        var1.set(data)
        window.update()
        gf.get_joke(var,window)


    elif 'book' in data:
        var1.set(data)
        window.update()
        bf.read_book(var,window)


    elif 'weather' in data:
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


    elif 'email' in data:
        var1.set(data)
        window.update()
        se.send_email(var,window,var1)

    elif 'sms' in data:
        var1.set(data)
        window.update()
        sf.send_sms()

    elif 'image' in data:
        var1.set(data)
        window.update()
        azure_a.read_image_text()

    elif "stop" in data:
        var1.set(data)
        window.update()
        print('Listening stopped')
        window.destroy()
    else:
        st.respond("Sorry! can you repeat .. ")
        data = st.listen().lower()
        digital_assistant(data)

############################ sendEmail ##################################
def start_ponit():

    data = st.listen().lower()
    digital_assistant(data)

################################# Tkinter ############################################


def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

################################# new features windows ############################################

def openNewWindow():
    newWindow = Toplevel(window)
    newWindow.title("Iris features")
    newWindow.geometry("500x350")
    Label(newWindow,text="Iris is here to help you, she can:", height = 3,  width = 500, font = "Courier" , bg = '#EEA47F').pack(pady = 10)
    Lb1 = Listbox(newWindow ,height = 200,width = 500,  bg = '#ADD8E6',activestyle = 'dotbox', font = "Courier" )
    Lb1.insert(1, "1.write your notes and read them for you.")
    Lb1.insert(2, "2.send emails.")
    Lb1.insert(3, "3.send SMS for any number your want." )
    Lb1.insert(4, "4.read a whole book just for you.")
    Lb1.insert(5, "5.read any text from any image.")
    Lb1.insert(6, "6.give you weather.")
    Lb1.insert(7, "7.give you time.")
    Lb1.insert(8, "8.open google or youtube.")
    Lb1.insert(9,"9.tell you a joke and make you smile:).")
    Lb1.pack()
    newWindow.mainloop()







label2 = Label(window, textvariable = var1, font = 3, wraplength = 500, bg = '#EEA47F')
label2.config(font=("Courier", 15))
var1.set('you Said:')
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

btn1 = Button(text = 'Click To Talk',height = 2,width = 13,command=start_ponit,  bg = '#031a45' ,	fg = '#fff')
btn1.config(font=("Courier", 12))
btn1.place(x = 385 , y =540)
btn2 = Button(text = 'Good Bye',height = 2,width = 13, command = window.destroy, bg = '#031a45' , fg = '#fff')
btn2.config(font=("Courier", 12))
btn2.place(x = 80 , y =540)
btn3 = Button(height = 2,width = 13, text ="My features",   command=openNewWindow ,bg = '#031a45' , fg = '#fff')
btn3.config(font=("Courier", 12))
btn3.place(x =233, y =540)

window.mainloop()
