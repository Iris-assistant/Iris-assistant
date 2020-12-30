from twilio.rest import Client
import speech_text as st
def send_sms():
    accounts ={
        'Aghyad':'+962785144005',
        'Rania':'+962785191344'
    }
    try:
        st.respond('enter a name ')
        name = st.listen()
        st.respond('enter a msg')
        massage = st.listen()
        sms_to =accounts[name]
        print(sms_to)
        account_sid = 'account_sid'
        auth_token = 'auth_token'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+12513256445',
            body=massage,
            to=sms_to
        )
        print(message.sid)
    except :
        send_sms()