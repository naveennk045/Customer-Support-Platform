import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def database():
    with open("db.txt", "r") as file:
        data = file.read()
    return data


conversation_history = [
    {"role": "system", "content": """Role: You are a friendly and professional customer support agent for Nature’s Cart, a UAE-based online grocery platform. Your job is to assist customers in a human-like, concise, and empathetic manner while maintaining a warm and helpful tone.
    Guidelines:
        Be Human & Conversational → Sound like a real person, not a bot. Use casual yet professional language.
        Concise Responses → Keep replies short and to the point while addressing customer concerns effectively.
        Empathetic & Friendly Tone → Show understanding and warmth (e.g., "I totally get it! Let me help.").
        Action-Oriented → Always guide the customer toward a solution in a clear way.
        Localized & Personalized → Address customers politely and use UAE-based references when needed.
        Avoid Technical Jargon → Keep language simple and easy to understand.
        if user asks about proce of the product then provide the price of the product randomly in uae dharams.dont say i dont know.
        """}
]


def llm_response(user_query: str) -> str:
    """
    Calls the Groq API to generate a response from the customer support agent while maintaining conversation history.

    Args:
        user_query (str): The customer's message.

    Returns:
        str: The AI-generated response.  
    """
    
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in environment variables.")

    client = Groq(api_key=api_key)

    try:
        # Append user query to history
        conversation_history.append({"role": "user", "content": user_query})

        # Call the API with full conversation history
        response = client.chat.completions.create(
            messages=conversation_history,
            model="llama-3.3-70b-versatile",
        )

        # Extract response text
        bot_response = response.choices[0].message.content.strip()

        # Append AI response to history
        conversation_history.append({"role": "assistant", "content": bot_response})

        return bot_response

    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing your request."

# Example usage:
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = llm_response(user_input)
        print(f"Bot: {response}")
    # print(database())
