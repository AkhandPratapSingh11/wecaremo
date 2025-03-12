import random
import logging

class WellnessSuggestions:
    SUGGESTIONS = {
        'very negative': [
            "It seems like you're going through a tough time. Would you like to talk about it?",
            "I'm here to support you. Consider reaching out to a professional counselor.",
            "Your feelings are valid. Let's explore some coping strategies together."
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

    @classmethod
    def get_suggestion(cls, sentiment):
        """
        Get a wellness suggestion based on sentiment
        """
        try:
            return random.choice(cls.SUGGESTIONS.get(sentiment, cls.SUGGESTIONS['neutral']))
        except Exception as e:
            logging.error(f"Wellness suggestion error: {e}")
            return "Take care of yourself."