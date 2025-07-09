# alerts.py - placeholder content

import os
from twilio.rest import Client

account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')
to_phone = os.getenv('DOCTOR_PHONE')
from_phone = os.getenv('TWILIO_PHONE')

client = Client(account_sid, auth_token)


def send_alert(message_body):
    message = client.messages.create(
        body=message_body,
        from_=from_phone,
        to=to_phone
    )
    return message.sid
