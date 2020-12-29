import speech_text as st
from tkinter.filedialog import *
import PyPDF2
import pyttsx3



def read_book(var,window):
    var.set("Here you go to book shelf\n")
    window.update()
    st.respond("Here you go to book shelf\n")
    book = askopenfilename()
    reader = PyPDF2.PdfFileReader(book)
    pages = reader.numPages
    for num in range(0, pages):
        page = reader.getPage(num)
        text = page.extractText()
        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()