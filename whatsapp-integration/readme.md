# 1️⃣ Clone the repo
git clone https://github.com/your-repo/whatsapp-fastapi.git
cd whatsapp-fastapi

# 2️⃣ Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Start FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# 5️⃣ Expose API publicly
ngrok http 8000

# 6️⃣ Set Twilio Webhook (Go to Twilio Console)
# URL: https://your-ngrok-url.io/whatsapp-webhook/

# 7️⃣ Send a test message via API
python -c "from utils import send_whatsapp_message; send_whatsapp_message('+1234567890', 'Hello!')"
