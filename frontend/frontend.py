# frontend/frontend.py
import streamlit as st
import logging
from backend.chatbot import EmoCareAssistant
from backend.sentiment_analyzer import SentimentAnalyzer
from backend.wellness_suggestion import WellnessSuggestions

# Configure page at the very beginning
st.set_page_config(
    page_title="EmoCare Assistant",
    page_icon="🌈",
    layout="wide"
)

class EmoCareInterface:
    def __init__(self):
        # Initialize components
        self.sentiment_analyzer = SentimentAnalyzer()
        self.wellness_suggester = WellnessSuggestions()
        self.chatbot = EmoCareAssistant()
        
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def render_sidebar(self):
        """
        Render application sidebar with additional information
        """
        st.sidebar.title("EmoCare Assistant")
        st.sidebar.info("""
        🤖 Your Emotional Wellness Companion
        
        Features:
        - Sentiment Analysis
        - Personalized Wellness Suggestions
        - Supportive Conversations
        """)

    def render_chat_interface(self):
        """
        Main chat interface rendering
        """
        # Title and description
        st.title("EmoCare: Your Emotional Wellness Assistant")
        st.write("Share your thoughts, and I'll provide supportive guidance.")

        # Initialize session state for chat history
        if 'messages' not in st.session_state:
            st.session_state.messages = []

        # Chat input
        user_input = st.chat_input("How are you feeling today?")

        # Process user input
        if user_input:
            try:
                # Add user message to chat history
                st.session_state.messages.append({
                    "role": "user", 
                    "content": user_input
                })

                # Process message through chatbot
                try:
                    response = self.chatbot.process_message(user_input)
                except Exception as process_error:
                    st.error(f"Error processing message: {process_error}")
                    self.logger.error(f"Message processing error: {process_error}")
                    return

                # Add AI response to chat history
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response.get('response', "I'm having trouble responding.")
                })

                # Display chat history
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

                # Display additional insights
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Sentiment", response.get('sentiment', 'N/A'))
                with col2:
                    st.success(f"Wellness Tip: {response.get('wellness_tip', 'Take care of yourself.')}")

            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
                self.logger.error(f"Chat processing error: {e}")

    def main(self):
        """
        Main application entry point
        """
        try:
            # Render sidebar
            self.render_sidebar()

            # Render chat interface
            self.render_chat_interface()

        except Exception as e:
            st.error(f"Application initialization error: {e}")
            self.logger.error(f"Initialization error: {e}")

def main():
    """
    Streamlit app entry point
    """
    try:
        app = EmoCareInterface()
        app.main()
    except Exception as e:
        st.error(f"Failed to start EmoCare: {e}")
        logging.error(f"Application startup error: {e}")

# Comprehensive Error Handling Wrapper
def run_app():
    try:
        main()
    except Exception as e:
        st.error(f"Critical Error: {e}")
        st.error("Please check the application logs for more details.")
        logging.critical(f"Unhandled exception: {e}", exc_info=True)

if __name__ == "__main__":
    run_app()