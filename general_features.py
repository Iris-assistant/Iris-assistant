import speech_text as st
import webbrowser
import pyjokes
from time import ctime

def open_youtube(var,window,var1):
    var.set('What are you looking for ? ')
    window.update()
    st.respond('What are you looking for ? ')
    query = st.listen()
    var1.set(query)
    window.update()
    webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
def open_google(var,window,var1):
    var.set('What are you looking for ? ')
    window.update()
    st.respond('What are you looking for ? ')
    query = st.listen()
    var1.set(query)
    window.update()
    webbrowser.open(f'https://www.google.com.tr/search?q={query}')

def get_joke(var,window):
    joke = pyjokes.get_joke()
    var.set(joke)
    window.update()
    st.respond(joke)
    st.respond('hahahaha')

def get_time(var,window):
    var.set(ctime())
    window.update()
    st.respond(ctime())
