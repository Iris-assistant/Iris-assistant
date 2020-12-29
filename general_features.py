import speech_text as st
import webbrowser
import pyjokes
from time import ctime
def open_youtube():
    st.respond("Here you go to Youtube\n")
    st.respond('is there any that may looking for ? ')
    query = st.listen()
    webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
def open_google():
    st.respond("Here you go to Google\n")
    st.respond('is there any that may looking for ? ')
    query = st.listen()
    webbrowser.open(f'https://www.google.com.tr/search?q={query}')

def get_joke():
    st.respond(pyjokes.get_joke())

def get_time():
    st.respond(ctime())
