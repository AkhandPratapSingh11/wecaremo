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
    
    # Chat input
    user_message = st.text_input("Share your thoughts and feelings...", key="user_input")
    
    if user_message:
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
        st.write("EmoCare:", result['response'])
        
        # Wellness Tip
        st.info(f"💡 Wellness Insight: {result['wellness_tip']}")

if __name__ == "__main__":
    main()