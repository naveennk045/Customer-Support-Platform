from fastapi import FastAPI, Form, Response
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.post("/whatsapp-webhook/")
async def whatsapp_webhook(From: str = Form(...), Body: str = Form(...)):
    response = MessagingResponse()
    response.message(f"Hello {From}, you said: {Body}")

    # Twilio expects XML, so return it with the correct content type
    return Response(content=str(response), media_type="application/xml")
