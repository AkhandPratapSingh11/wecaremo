import random

class WellnessSuggestion:
    """
    Provides wellness recommendations based on sentiment analysis.
    """

    def __init__(self):
        """
        Initializes the wellness suggestion system with predefined recommendations.
        """
        self.suggestions = {
            "positive": [
                "Keep up the great work! How about celebrating with a small treat?",
                "You're doing amazing! Maybe take a nature walk to enhance your mood.",
                "Stay motivated! Practicing gratitude can further boost your positivity."
            ],
            "neutral": [
                "It’s okay to feel neutral sometimes. A short meditation could help.",
                "Journaling your thoughts might help bring more clarity to your day.",
                "Try listening to music or doing a simple breathing exercise."
            ],
            "negative": [
                "It’s okay to have tough days. Talking to a friend might help.",
                "Deep breathing or a short relaxation exercise could improve your mood.",
                "Consider a quick physical activity like stretching or a walk to ease stress."
            ]
        }

    def get_suggestion(self, sentiment: str) -> str:
        """
        Provides a wellness suggestion based on the detected sentiment.
        
        Args:
            sentiment (str): The analyzed sentiment (positive, neutral, or negative).
        
        Returns:
            str: A wellness suggestion.
        """
        return random.choice(self.suggestions.get(sentiment, ["Stay mindful and take care of yourself."]))

# Example Usage
if __name__ == "__main__":
    wellness = WellnessSuggestion()
    print("Wellness Tip:", wellness.get_suggestion("negative"))
