from twilio.rest import Client
from apis.config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to: str, message: str):
    to = f"whatsapp:{to}"
    msg = client.messages.create(from_=TWILIO_WHATSAPP_NUMBER, body=message, to=to)
    return msg.sid
