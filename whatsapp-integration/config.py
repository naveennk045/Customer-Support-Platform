import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio Sandbox Number
