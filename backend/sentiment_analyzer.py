import logging
import re
from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary NLTK resources
try:
    nltk.download('vader_lexicon', quiet=True)
except:
    logging.warning("Could not download VADER lexicon")

class SentimentAnalyzer:
    def __init__(self):
        # Multiple sentiment analysis tools
        self.textblob_analyzer = TextBlob
        self.vader_analyzer = SentimentIntensityAnalyzer()
        
        # Emotional keyword dictionaries
        self.emotion_keywords = {
            'anxiety': ['worry', 'anxious', 'stress', 'panic', 'afraid'],
            'depression': ['sad', 'depressed', 'hopeless', 'lonely', 'worthless'],
            'anger': ['angry', 'frustrated', 'irritated', 'furious', 'rage'],
            'joy': ['happy', 'excited', 'grateful', 'delighted', 'joyful'],
            'calm': ['peaceful', 'relaxed', 'serene', 'tranquil', 'content']
        }

    def preprocess_text(self, text):
        """
        Clean and preprocess input text
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and extra whitespaces
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

    def detect_specific_emotion(self, text):
        """
        Detect specific emotional undertones
        """
        text = self.preprocess_text(text)
        
        for emotion, keywords in self.emotion_keywords.items():
            if any(keyword in text for keyword in keywords):
                return emotion
        
        return 'neutral'

    def analyze_sentiment(self, text):
        """
        Comprehensive sentiment analysis with multiple techniques
        """
        try:
            # Preprocess text
            cleaned_text = self.preprocess_text(text)
            
            # TextBlob Analysis
            blob = self.textblob_analyzer(cleaned_text)
            textblob_polarity = blob.sentiment.polarity
            
            # VADER Analysis
            vader_scores = self.vader_analyzer.polarity_scores(text)
            vader_compound = vader_scores['compound']
            
            # Specific emotion detection
            specific_emotion = self.detect_specific_emotion(text)
            
            # Combine multiple sentiment indicators
            def categorize_sentiment(polarity):
                if polarity > 0.5:
                    return 'very positive', 'green'
                elif 0.1 < polarity <= 0.5:
                    return 'positive', 'light green'
                elif -0.1 <= polarity <= 0.1:
                    return 'neutral', 'gray'
                elif -0.5 <= polarity < -0.1:
                    return 'negative', 'light red'
                else:
                    return 'very negative', 'red'
            
            # Weighted average of sentiment scores
            combined_polarity = (textblob_polarity + vader_compound) / 2
            
            sentiment, color = categorize_sentiment(combined_polarity)
            
            return {
                'sentiment': sentiment,
                'polarity': combined_polarity,
                'color': color,
                'specific_emotion': specific_emotion,
                'textblob_score': textblob_polarity,
                'vader_score': vader_compound
            }
        
        except Exception as e:
            logging.error(f"Sentiment analysis error: {e}")
            return {
                'sentiment': 'neutral',
                'polarity': 0,
                'color': 'gray',
                'specific_emotion': 'neutral',
                'textblob_score': 0,
                'vader_score': 0
            }

# Debugging and testing function
def test_sentiment_analyzer():
    analyzer = SentimentAnalyzer()
    
    test_texts = [
        "I'm feeling really happy and excited today!",
        "I'm worried about my upcoming exams and feeling stressed.",
        "Everything is going well, I feel calm and peaceful.",
        "I'm frustrated with my current situation.",
        "Neutral statement without strong emotions."
    ]
    
    for text in test_texts:
        result = analyzer.analyze_sentiment(text)
        print(f"\nText: {text}")
        print("Sentiment Analysis Result:")
        for key, value in result.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    test_sentiment_analyzer()