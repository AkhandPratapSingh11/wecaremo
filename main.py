import streamlit as st
from backend.chatbot import Chatbot
from backend.memory import ConversationMemory
from backend.model import AIModel
from backend.wellness_suggestion import WellnessSuggestion

# Initialize components
memory = ConversationMemory()
chatbot = Chatbot()
ai_model = AIModel()
wellness = WellnessSuggestion()

# Streamlit UI
st.set_page_config(page_title="EmoCare - AI Wellness Assistant", layout="wide")
st.title("🤖 EmoCare: Your AI-Powered Wellness Companion")

# Sidebar for user session details
st.sidebar.header("User Settings")
user_name = st.sidebar.text_input("Enter your name:", "Guest")
st.sidebar.markdown(f"**Welcome, {user_name}!**")

# Chat input area
st.write("### Chat with EmoCare")
user_input = st.text_input("Type your message here...", key="user_input")

if user_input:
    # Store user input in memory
    memory.store_message({"role": "user", "content": user_input})

    # Get AI response
    ai_response, sentiment = ai_model.generate_response(user_input)
    
    # Store AI response
    memory.store_message({"role": "assistant", "content": ai_response})

    # Display conversation
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(ai_response)

    # Provide wellness suggestion if sentiment is negative or neutral
    if sentiment in ["negative", "neutral"]:
        suggestion = wellness.get_suggestion(sentiment)
        st.markdown(f"💡 **Wellness Tip:** {suggestion}")

# Show conversation history
st.write("### Chat History")
for msg in memory.get_messages():
    st.chat_message(msg["role"]).write(msg["content"])
