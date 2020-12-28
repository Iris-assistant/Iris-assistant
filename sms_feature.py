from twilio.rest import Client

def send_sms():
    accounts ={
        'Aghyad':'+962785144005',
        'Rania':'+962785191344'
    }
    try:
        name = input('enter a name ')
        massage = input('enter a msg')
        sms_to =accounts[name]
        print(sms_to)
        account_sid = 'AC8d208345b04c4a4dd91adee3bb426b0f'
        auth_token = 'e2ed66b7440dba6694dd3c0b2f3cd7b5'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+12513256445',
            body=massage,
            to=sms_to
        )

        print(message.sid)

    except :
        send_sms()