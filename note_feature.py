import speech_text as st
import datetime

def write_note():
    st.respond("What should i write, sir")
    note = st.listen()
    file = open('iris.txt', 'w')
    st.respond("Sir, Should i include date and time")
    snfm = st.listen()
    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
    else:
        file.write(note)

def show_note():
    st.respond("Showing Notes")
    file = open("iris.txt", "r")
    print(file.read())
    st.respond(file.read(6))