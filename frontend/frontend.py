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

    def render_sidebar(self, sentiment_result=None):
        """
        Render application sidebar with sentiment and wellness information
        """
        st.sidebar.title("EmoCare Assistant")
        
        # Sentiment Analysis Section
        st.sidebar.header("🌈 Sentiment Insights")
        
        if sentiment_result:
            # Sentiment Visualization
            sentiment = sentiment_result.get('sentiment', 'N/A')
            polarity = sentiment_result.get('polarity', 0)
            color = sentiment_result.get('color', 'gray')
            specific_emotion = sentiment_result.get('specific_emotion', 'N/A')
            
            # Sentiment Emoji Mapping
            sentiment_emojis = {
                'very negative': '😫',
                'negative': '😔',
                'neutral': '😐',
                'positive': '😊',
                'very positive': '😄'
            }
            
            # Display Sentiment Details
            st.sidebar.markdown(f"""
            ### Current Emotional State
            
            **Sentiment:** {sentiment_emojis.get(sentiment, '🤔')} {sentiment.title()}
            
            **Emotional Depth:**
            - Polarity: {polarity:.2f}
            - Specific Emotion: {specific_emotion.title()}
            
            **Sentiment Intensity:**
            {"▇" * int(abs(polarity) * 5)}
            """)
            
            # Color-coded Sentiment Bar
            st.sidebar.markdown(f"""
            <div style="background-color:{color};height:10px;width:100%;"></div>
            """, unsafe_allow_html=True)
        
        # Wellness Information Section
        st.sidebar.header("🌟 Wellness Tips")
        st.sidebar.info("""
        Emotional well-being is a journey.
        
        - Practice self-compassion
        - Stay mindful
        - Seek support when needed
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
        
        # Initialize session state for last sentiment
        if 'last_sentiment' not in st.session_state:
            st.session_state.last_sentiment = None

        # Render existing messages in the main bar
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input
        user_input = st.chat_input("How are you feeling today?")

        # Process user input
        if user_input:
            try:
                # Add user message to chat history and display
                st.session_state.messages.append({
                    "role": "user", 
                    "content": user_input
                })
                with st.chat_message("user"):
                    st.markdown(user_input)

                # Process message through chatbot
                response = self.process_message(user_input)

                # Render sidebar with sentiment
                self.render_sidebar(
                    sentiment_result=st.session_state.get('last_sentiment')
                )

            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
                self.logger.error(f"Chat processing error: {e}")

        else:
            # Render sidebar even without new messages
            self.render_sidebar(
                sentiment_result=st.session_state.get('last_sentiment')
            )

    def process_message(self, user_input):
        """
        Process user message and handle response
        """
        try:
            # Process message through chatbot
            response = self.chatbot.process_message(user_input)
            
            # Store sentiment for sidebar
            st.session_state.last_sentiment = {
                'sentiment': response.get('sentiment', 'N/A'),
                'polarity': response.get('polarity', 0),
                'color': response.get('sentiment_color', 'gray'),
                'specific_emotion': response.get('specific_emotion', 'N/A')
            }

            # Add AI response to chat history and display
            st.session_state.messages.append({
                "role": "assistant", 
                "content": response.get('response', "I'm having trouble responding.")
            })
            with st.chat_message("assistant"):
                st.markdown(response.get('response', "I'm having trouble responding."))

            return response

        except Exception as process_error:
            st.error(f"Error processing message: {process_error}")
            self.logger.error(f"Message processing error: {process_error}")
            return None

    def main(self):
        """
        Main application entry point
        """
        try:
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