import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')
def respond(audioString):
    """

    :rtype: object
    """
    try:
        print(audioString)
        engine.say(audioString)
        engine.runAndWait()
    except Exception:
        pass


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    data = "def_msg"
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
        respond("Sorry! can you repeat .. ")
        return listen()
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data