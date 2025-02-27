# AIChatSupport Platform

AIChatSupport is a comprehensive platform designed to create, deploy, and manage AI-powered customer support chatbots. This project includes both frontend and backend components, as well as WhatsApp integration.

## Project Structure

```plaintext
Customer-Support-Platform/
│── backend/                     # Backend Service (FastAPI)
│   ├── __pycache__/             # Auto-generated Python cache (ignored)
│   ├── .env                     # Environment variables (e.g., DB credentials)
│   ├── config.py                # Configuration settings (e.g., DB connection)
│   ├── main.py                  # FastAPI application entry point
│   ├── requirements.txt         # Python dependencies
│   ├── utils.py                 # Utility functions (e.g., DB helpers)
│   ├── db.sql                   # SQL schema for MySQL
│   ├── models.py                # Database models (SQLAlchemy, Pydantic)
│   ├── routers/                 # API Routes
│   │   ├── auth.py              # Authentication routes
│   │   ├── user.py              # User-related routes
│   │   ├── tickets.py           # Ticket handling routes
│   │   └── whatsapp.py          # WhatsApp API routes
│   ├── services/                # Business logic services
│   │   ├── auth_service.py      # Authentication logic
│   │   ├── user_service.py      # User service logic
│   │   ├── ticket_service.py    # Ticket processing logic
│   │   └── whatsapp_service.py  # WhatsApp integration logic
│   ├── middlewares/             # Middleware (e.g., logging, security)
│   ├── tests/                   # Unit and integration tests
│   └── docs/                    # API Documentation
│
│── frontend/                     # Frontend Service (HTML, CSS, JS)
│   ├── assets/                   # Static assets (images, icons, fonts)
│   │   └── dashboard.png         # Example image
│   ├── static/                   # Static files (CSS, JS, etc.)
│   │   ├── DashBoard/            # Dashboard-related files
│   │   │   ├── DashBoard.css     # Dashboard styles
│   │   │   ├── DashBoard.html    # Dashboard page
│   │   │   └── DashBoard.js      # Dashboard scripts
│   │   ├── SignInPage/           # Sign-in/Sign-up-related files
│   │   │   ├── SignInPage.css    # Sign-in/Sign-up styles
│   │   │   ├── SignInPage.html   # Sign-in/Sign-up page
│   │   │   └── SignInPage.js     # Sign-in/Sign-up scripts
│   ├── index.html                # Main entry point (if needed)
│
│── whatsapp-integration/         # WhatsApp Integration Module (if applicable)
│   ├── __pycache__/              # Auto-generated Python cache (ignored)
│   ├── main.py                   # WhatsApp integration logic
│   ├── config.py                 # WhatsApp config (API keys, settings)
│   ├── utils.py                  # Helper functions for WhatsApp API
│   ├── handlers.py                # Message processing logic
│   └── readme.md                 # Documentation for this module
│
│── tests/                        # Testing Directory (unit & integration tests)
│   ├── backend/                  # Backend test cases
│   ├── frontend/                 # Frontend test cases (UI, JS)
│   ├── whatsapp-integration/     # WhatsApp module tests
│
│── docs/                         # Documentation (Swagger, Postman)
│   ├── API_reference.md          # API Documentation
│   ├── setup_guide.md            # Setup and installation guide
│   ├── architecture.md           # System architecture details
│
│── .gitignore                     # Git ignore file
│── README.md                      # Project Overview and Guide
```

3. **Install dependencies:**

    ```sh
    pip install -r whatsapp-integration/requirements.txt
    ```

4. **Set up the database:**

    - Create a MySQL database using the script in [db.sql](http://_vscodecontentref_/16).

5. **Configure environment variables:**

    - Create a `.env` file in the [whatsapp-integration](http://_vscodecontentref_/17) directory with the following content:

    ```env
    TWILIO_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    ```

6. **Run the backend server:**

    ```sh
    uvicorn backend.main:app --reload
    ```

### Frontend Setup

1. **Navigate to the frontend directory:**

    ```sh
    cd frontend
    ```

2. **Start the frontend server:**

    ```sh
    python -m http.server 3000
    ```

### WhatsApp Integration

1. **Expose the API publicly using ngrok:**

    ```sh
    ngrok http 8000
    ```

2. **Set the Twilio Webhook:**

    - Go to the Twilio Console and set the webhook URL to `https://your-ngrok-url.io/whatsapp-webhook/`.

3. **Send a test message via API:**

    ```sh
    python -c "from utils import send_whatsapp_message; send_whatsapp_message('+1234567890', 'Hello!')"
    ```

## Usage

- Access the frontend at `http://localhost:3000`.
- Sign in or sign up to use the platform.
- Configure database and Twilio credentials via the dashboard.
- Deploy and manage your AI chatbots.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.