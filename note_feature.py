import speech_text as st
import datetime

def write_note(var,window,var1):
    var.set("What should i write, sir")
    window.update()
    st.respond("What should i write, sir")
    note = st.listen()
    var1.set(note)
    window.update()
    file = open('iris.txt', 'w')
    var.set("Sir, Should i include date and time")
    window.update()
    st.respond("Sir, Should i include date and time")
    snfm = st.listen()
    var1.set(snfm)
    window.update()
    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
    else:
        file.write(note)
def show_note(var,window):
    var.set("Showing Notes")
    window.update()
    st.respond("Showing Notes")
    file = open("iris.txt", "r")
    var.set(file.read())
    window.update()
    print(file.read())
    st.respond(file.read(6))