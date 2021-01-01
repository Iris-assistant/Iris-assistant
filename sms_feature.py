from twilio.rest import Client
import speech_text as st

def send_sms():
    try:
        accounts ={
            'a':'+962785144005',
            's':'+962785191344'
        }

        st.respond('enter a name ')
        name = st.listen().lower()
        sms_to =accounts[name[0]]
        get_msg(sms_to)
    except Exception:
        send_sms()



def get_msg(sms_to):
    st.respond('enter a msg')
    massage = st.listen()
    print(massage,'22')
    send_msg(massage, sms_to)





def send_msg(massage,sms_to):
    print(massage,'30')
    # if massage == " ":
    #     massage = "defualt massage"

    account_sid = 'AC8d208345b04c4a4dd91adee3bb426b0f'
    auth_token = '8cd5b2dbefc525167abcbdc25c0f70e8'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12513256445',
        body=massage,
        to=sms_to
    )