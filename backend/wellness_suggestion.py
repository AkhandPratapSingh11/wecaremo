import logging
import random
import os
from dotenv import load_dotenv

class WellnessSuggestions:
    def __init__(self):
        # Comprehensive suggestion database
        self.suggestions = {
            'very negative': [
                "It seems like you're going through a tough time. Would you like to talk about it?",
                "Your feelings are valid. Consider reaching out for support.",
                "During difficult moments, be gentle with yourself."
            ],
            'negative': [
                "Take a deep breath. Things will get better.",
                "Practice self-compassion during difficult moments.",
                "Consider a short meditation or mindfulness exercise."
            ],
            'neutral': [
                "How about trying a quick mood-boosting activity?",
                "Stay mindful and present in the moment.",
                "Small steps can lead to positive changes."
            ],
            'positive': [
                "Great to hear you're feeling good! Keep maintaining this positive energy.",
                "Continue nurturing your mental well-being.",
                "Reflect on what's making you feel positive today."
            ],
            'very positive': [
                "Your positive outlook is inspiring! Keep shining!",
                "Celebrate your emotional resilience.",
                "Share your positivity with others around you."
            ]
        }
        
        # Try to load LLM for advanced suggestions
        try:
            from groq import Groq
            load_dotenv()
            self.groq_client = Groq(api_key=os.getenv('GROQ_API_KEY', ''))
            self.use_llm = True
        except Exception as e:
            logging.warning(f"LLM not available: {e}")
            self.groq_client = None
            self.use_llm = False

    def get_suggestion(self, sentiment_result):
        """
        Generate personalized wellness suggestion
        """
        try:
            # Extract sentiment
            sentiment = sentiment_result.get('sentiment', 'neutral')
            
            # Select suggestions for the sentiment
            suggestions = self.suggestions.get(sentiment, self.suggestions['neutral'])
            
            # Randomly choose a suggestion
            suggestion = random.choice(suggestions)
            
            # Optional LLM enhancement
            if self.use_llm:
                enhanced_suggestion = self._generate_llm_suggestion(sentiment)
                if enhanced_suggestion:
                    suggestion = enhanced_suggestion
            
            return suggestion
        
        except Exception as e:
            logging.error(f"Wellness suggestion error: {e}")
            return "Take care of yourself. Your well-being matters."

    def _generate_llm_suggestion(self, sentiment):
        """
        Generate suggestion using LLM
        """
        if not self.use_llm or not self.groq_client:
            return None

        try:
            response = self.groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a compassionate wellness coach providing personalized mental health support."
                    },
                    {
                        "role": "user",
                        "content": f"Generate a wellness suggestion for someone feeling {sentiment}. The suggestion should be supportive, actionable, and empathetic."
                    }
                ],
                model="qwen-2.5-32b",
                temperature=0.7,
                max_tokens=200
            )

            suggestion = response.choices[0].message.content.strip()
            return suggestion

        except Exception as e:
            logging.error(f"LLM suggestion generation error: {e}")
            return None

# Debugging function
def test_wellness_suggestions():
    from backend.sentiment_analyzer import SentimentAnalyzer
    
    analyzer = SentimentAnalyzer()
    wellness_suggester = WellnessSuggestions()
    
    test_texts = [
        "I'm feeling really happy and excited today!",
        "I'm worried about my upcoming exams and feeling stressed.",
        "Everything is going well, I feel calm and peaceful.",
        "I'm frustrated with my current situation.",
        "Neutral statement without strong emotions."
    ]
    
    for text in test_texts:
        sentiment_result = analyzer.analyze_sentiment(text)
        suggestion = wellness_suggester.get_suggestion(sentiment_result)
        
        print(f"\nText: {text}")
        print(f"Sentiment: {sentiment_result['sentiment']}")
        print(f"Suggestion: {suggestion}")

if __name__ == "__main__":
    test_wellness_suggestions()