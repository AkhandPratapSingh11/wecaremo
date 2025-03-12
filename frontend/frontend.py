import streamlit as st
import plotly.graph_objs as go
from backend.chatbot import EmoCareAssistant

def create_sentiment_gauge(sentiment, polarity):
    """
    Create an interactive sentiment gauge
    """
    sentiment_map = {
        'very negative': 0,
        'negative': 25,
        'neutral': 50,
        'positive': 75,
        'very positive': 100
    }
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=sentiment_map.get(sentiment, 50),
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Emotional Wellness"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 25], 'color': "red"},
                {'range': [25, 50], 'color': "orange"},
                {'range': [50, 75], 'color': "yellow"},
                {'range': [75, 100], 'color': "green"}
            ]
        }
    ))
    
    st.plotly_chart(fig)

def main():
    st.set_page_config(
        page_title="EmoCare - Wellness Assistant",
        page_icon="❤️",
        layout="centered"
    )
    
    st.title("🌈 EmoCare: Your Emotional Wellness Companion")
    
    # Initialize session state
    if 'assistant' not in st.session_state:
        st.session_state.assistant = EmoCareAssistant()
    
    # Initialize conversation history in session state
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []

    # Display conversation history
    for message in st.session_state.conversation_history:
        if message['role'] == 'user':
            st.chat_message("user").write(message['content'])
        else:
            st.chat_message("assistant").write(message['content'])

    # Chat input
    user_message = st.chat_input("Share your thoughts and feelings...")
    
    if user_message:
        # Add user message to conversation history
        st.session_state.conversation_history.append({
            'role': 'user',
            'content': user_message
        })
        
        # Display user message
        st.chat_message("user").write(user_message)
        
        # Process message
        result = st.session_state.assistant.process_message(user_message)
        
        # Sentiment Gauge
        create_sentiment_gauge(result['sentiment'], result['polarity'])
        
        # Sentiment Display
        st.markdown(f"""
        **Emotional State:** 
        <span style='color:{result['sentiment_color']};font-weight:bold'>
        {result['sentiment'].upper()}
        </span>
        """, unsafe_allow_html=True)
        
        # AI Response
        ai_response = result['response']
        st.chat_message("assistant").write(ai_response)
        
        # Add AI response to conversation history
        st.session_state.conversation_history.append({
            'role': 'assistant',
            'content': ai_response
        })
        
        # Wellness Tip
        st.info(f"💡 Wellness Insight: {result['wellness_tip']}")

if __name__ == "__main__":
    main()