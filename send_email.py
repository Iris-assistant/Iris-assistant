import speech_text as st
import smtplib

def send_email():
    try:
        st.respond("What should I say?")
        content = st.listen()
        st.respond("whome should i send")
        to = input()
        sendEmail(to, content)
        st.respond("Email has been sent !")
    except Exception as e:
        print(e)
        st.respond("I am not able to send this email")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('iris.assistant2020@gmail.com', 'iris2020')
    server.sendmail('iris.asssistant2020@gmail.com', to, content)
    server.close()
