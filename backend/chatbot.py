from .model import EmoCareModel
from .sentiment_analyzer import SentimentAnalyzer
from .wellness_suggestion import WellnessSuggestions
import logging

class EmoCareAssistant:
    def __init__(self):
        self.model = EmoCareModel()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.wellness_suggester = WellnessSuggestions()
        self.conversation_history = []

    def process_message(self, user_message):
        """
        Process user message and generate comprehensive response
        """
        try:
            # Analyze sentiment
            sentiment_result = self.sentiment_analyzer.analyze_sentiment(user_message)
            
            # Prepare context (last 5 messages)
            context = "\n".join([
                f"{msg['role'].capitalize()}: {msg['content']}" 
                for msg in self.conversation_history[-5:]
            ])
            
            # Generate AI response with context
            ai_response = self.model.generate_response(context, user_message)
            
            # Get wellness suggestion
            wellness_tip = self.wellness_suggester.get_suggestion(sentiment_result['sentiment'])
            
            return {
                'response': ai_response,
                'sentiment': sentiment_result['sentiment'],
                'sentiment_color': sentiment_result['color'],
                'wellness_tip': wellness_tip,
                'polarity': sentiment_result['polarity']
            }
        except Exception as e:
            logging.error(f"Message processing error: {e}")
            return {
                'response': "I'm having trouble processing your message.",
                'sentiment': 'neutral',
                'sentiment_color': 'gray',
                'wellness_tip': "Take a moment to breathe and relax.",
                'polarity': 0
            }