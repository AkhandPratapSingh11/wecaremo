import os
import groq
from memory import ConversationMemory
from wellness_suggestion import get_wellness_suggestion
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq AI Client
client = groq.Client(api_key=GROQ_API_KEY)

# Initialize conversation memory
memory = ConversationMemory()

def generate_response(user_input: str) -> str:
    """
    Generates an AI-powered response based on user input.
    
    Args:
        user_input (str): The user's message.
    
    Returns:
        str: AI-generated response.
    """
    try:
        # Retrieve chat history
        chat_history = memory.get_chat_history()

        # Format the conversation for context
        conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])
        prompt = f"{conversation}\nUser: {user_input}\nAI:"

        # Generate response using Groq API
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        ai_response = response.choices[0].message["content"].strip()

        # Save conversation in memory
        memory.save_message("User", user_input)
        memory.save_message("AI", ai_response)

        # Check for wellness suggestions
        wellness_tip = get_wellness_suggestion(user_input)
        if wellness_tip:
            ai_response += f"\n\n💡 Wellness Tip: {wellness_tip}"

        return ai_response

    except Exception as e:
        return f"⚠️ An error occurred: {str(e)}"

