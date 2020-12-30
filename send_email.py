import speech_text as st
import smtplib
contacts={'b':'aghyadalbalkhi@gmail.com','r':'raniaabdullah6600@gmail.com','f':'farahalzuot97@gmail.com','s':'sajanader93@gmail.com'}
def send_email(var,window,var1):
    try:
        var.set("What should I say?")
        window.update()
        st.respond("What should I say?")
        content = st.listen()
        var1.set(content)
        window.update()
        # var.set("whome should I send")
        # window.update()
        whome_send(content,var,window,var1)
    except Exception :
        send_email(var, window, var1)


def whome_send(content,var,window,var1):
    try:
        st.respond("whome should I send")
        to = st.listen()[0].lower()
        while to not in contacts:
            st.respond("i could not find the contact !")
            to = st.listen()[0].lower()
        sendEmail(contacts[to], content)
        st.respond("Email has been sent !")

    except Exception as e:
        print(e)
        var.set("I am not able to send this email")
        window.update()
        st.respond("I am not able to send this email")
        whome_send(content,var,window,var1)



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('iris.assistant2020@gmail.com', 'iris2020')
    server.sendmail('iris.asssistant2020@gmail.com', to, content)
    server.close()