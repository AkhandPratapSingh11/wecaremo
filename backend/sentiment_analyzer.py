from textblob import TextBlob
import logging

class SentimentAnalyzer:
    @staticmethod
    def analyze_sentiment(text):
        """
        Analyze sentiment of user message with detailed categorization
        """
        try:
            # Use TextBlob for sentiment analysis
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            
            # Detailed sentiment categorization
            if polarity > 0.5:
                sentiment = 'very positive'
                color = 'green'
            elif 0.1 < polarity <= 0.5:
                sentiment = 'positive'
                color = 'light green'
            elif -0.1 <= polarity <= 0.1:
                sentiment = 'neutral'
                color = 'gray'
            elif -0.5 <= polarity < -0.1:
                sentiment = 'negative'
                color = 'light red'
            else:
                sentiment = 'very negative'
                color = 'red'
            
            return {
                'sentiment': sentiment,
                'polarity': polarity,
                'color': color
            }
        except Exception as e:
            logging.error(f"Sentiment analysis error: {e}")
            return {
                'sentiment': 'neutral',
                'polarity': 0,
                'color': 'gray'
            }