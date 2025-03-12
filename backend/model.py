import os
import requests

class AIModel:
    """
    Handles interaction with the Groq API for generating AI responses.
    """

    def __init__(self, api_key: str):
        """
        Initializes the AI model with the provided Groq API key.
        
        Args:
            api_key (str): Groq API authentication key.
        """
        self.api_key = api_key
        self.api_url = "https://api.groq.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate_response(self, prompt: str, chat_history: list):
        """
        Sends a request to Groq's API and retrieves an AI-generated response.
        
        Args:
            prompt (str): The user's input message.
            chat_history (list): The conversation history for context.
        
        Returns:
            str: AI-generated response.
        """
        payload = {
            "model": "llama3-8b",  # Adjust based on available Groq models
            "messages": chat_history + [{"role": "user", "content": prompt}],
            "max_tokens": 300
        }

        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response_data = response.json()

            # Extract AI response
            if response.status_code == 200 and "choices" in response_data:
                return response_data["choices"][0]["message"]["content"]
            else:
                return "I'm sorry, but I couldn't generate a response at the moment."
        
        except Exception as e:
            return f"Error communicating with AI model: {str(e)}"
