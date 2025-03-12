import streamlit as st
from chatbot import get_response

# Streamlit Page Configuration
st.set_page_config(page_title="EmoCare - AI Wellness Assistant", page_icon="💙", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .reportview-container {
            background: #f0f2f6;
        }
        .chat-container {
            max-width: 700px;
            margin: auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .user-msg {
            background-color: #DCF8C6;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
            width: fit-content;
        }
        .bot-msg {
            background-color: #EAEAEA;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
            width: fit-content;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize Chat Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Header
st.title("💙 EmoCare - Your AI Wellness Companion")
st.write("🤖 Type your thoughts, and I'll offer **emotional support** & **wellness suggestions**.")

# Chat UI
with st.container():
    for entry in st.session_state.chat_history:
        if entry["role"] == "user":
            st.markdown(f"<div class='user-msg'>{entry['message']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-msg'>{entry['message']}</div>", unsafe_allow_html=True)

# User Input
user_input = st.text_input("💬 Your Message:", key="user_input")

if st.button("Send", key="send_btn"):
    if user_input.strip():
        # Store User Message
        st.session_state.chat_history.append({"role": "user", "message": user_input})

        # Get AI Response
        bot_response = get_response(user_input)

        # Store AI Response
        st.session_state.chat_history.append({"role": "bot", "message": bot_response})

        # Refresh the page to show new messages
        st.experimental_rerun()
