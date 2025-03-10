from fastapi import FastAPI, Form, Response
from twilio.twiml.messaging_response import MessagingResponse
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.llm import llm_response
import uvicorn

app = FastAPI()

@app.post("/whatsapp-webhook/")
async def whatsapp_webhook(From: str = Form(...), Body: str = Form(...)):
    response = MessagingResponse()
    print(f"Received message from {From}: {Body}")
    llm_response_text = llm_response(Body)
    response.message(llm_response_text)
    return Response(content=str(response), media_type="application/xml")
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)