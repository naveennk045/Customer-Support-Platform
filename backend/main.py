from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# to run - py -m uvicorn main:app --reload

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add CORS middleware to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': '7261',  # Replace with your MySQL password
    'database': 'demo_app'
}

# Pydantic models for request validation
class LoginData(BaseModel):
    email: str
    password: str

class SignupData(BaseModel):
    company_name: str
    email: str
    password: str

class TwilioCredentials(BaseModel):
    accountSid: str
    authToken: str
    phoneNumber: str
    enableWhatsApp: bool

class DBCredentials(BaseModel):
    dbType: str
    dbHost: str
    dbPort: str
    dbName: str
    dbUsername: str
    dbPassword: str

class ChatbotSettings(BaseModel):
    chatbotName: str
    chatbotGreeting: str
    chatbotTheme: str

# Database connection helper
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Endpoints
@app.post("/api/login")  # LOGIN_ENDPOINT
async def login(login_data: LoginData):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s",
            (login_data.email, login_data.password)
        )
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"access_token": f"demo_token_{user['id']}"}  # Simple token for demo
    finally:
        cursor.close()
        conn.close()

@app.post("/api/signup")  # SIGNUP_ENDPOINT
async def signup(signup_data: SignupData):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Check if email already exists
        cursor.execute("SELECT id FROM users WHERE email = %s", (signup_data.email,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Email already registered")
        
        cursor.execute(
            "INSERT INTO users (company_name, email, password) VALUES (%s, %s, %s)",
            (signup_data.company_name, signup_data.email, signup_data.password)
        )
        conn.commit()
        return {"detail": "Registration successful"}
    finally:
        cursor.close()
        conn.close()

@app.post("/api/save-twilio-credentials")
async def save_twilio_credentials(credentials: TwilioCredentials):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO twilio_credentials (account_sid, auth_token, phone_number, enable_whatsapp)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
            auth_token = %s, phone_number = %s, enable_whatsapp = %s
            """,
            (credentials.accountSid, credentials.authToken, credentials.phoneNumber, 
             credentials.enableWhatsApp, credentials.authToken, credentials.phoneNumber, 
             credentials.enableWhatsApp)
        )
        conn.commit()
        return {"success": True}
    finally:
        cursor.close()
        conn.close()

@app.post("/api/save-db-credentials")
async def save_db_credentials(credentials: DBCredentials):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO db_credentials (db_type, db_host, db_port, db_name, db_username, db_password)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
            db_host = %s, db_port = %s, db_name = %s, db_username = %s, db_password = %s
            """,
            (credentials.dbType, credentials.dbHost, credentials.dbPort, credentials.dbName,
             credentials.dbUsername, credentials.dbPassword, credentials.dbHost, 
             credentials.dbPort, credentials.dbName, credentials.dbUsername, credentials.dbPassword)
        )
        conn.commit()
        return {"success": True}
    finally:
        cursor.close()
        conn.close()

@app.post("/api/save-chatbot-settings")
async def save_chatbot_settings(settings: ChatbotSettings):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO chatbot_settings (chatbot_name, chatbot_greeting, chatbot_theme)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE 
            chatbot_greeting = %s, chatbot_theme = %s
            """,
            (settings.chatbotName, settings.chatbotGreeting, settings.chatbotTheme,
             settings.chatbotGreeting, settings.chatbotTheme)
        )
        conn.commit()
        return {"success": True}
    finally:
        cursor.close()
        conn.close()

# Run the app: uvicorn main:app --reload