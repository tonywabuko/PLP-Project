# alerts.py

import os
from dotenv import load_dotenv  # ✅ Add this line
from twilio.rest import Client

load_dotenv()  # ✅ This loads values from the .env file

# Get environment variables
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')
to_phone = os.getenv('DOCTOR_PHONE')
from_phone = os.getenv('TWILIO_PHONE')

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Function to send alert
def send_alert(message_body):
    message = client.messages.create(
        body=message_body,
        from_=from_phone,
        to=to_phone
    )
    return message.sid

