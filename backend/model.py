import os
from groq import Groq
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmoCareModel:
    def __init__(self):
        try:
            load_dotenv()
            self.client = Groq(
                api_key=os.getenv('GROQ_API_KEY', '')
            )
            self.model = "qwen-2.5-32b"
            logger.info("EmoCare Model initialized successfully")
        except Exception as e:
            logger.error(f"Model initialization error: {e}")
            raise

    def generate_response(self, context, user_message):
        """
        Generate empathetic response using Groq Qwen model
        """
        try:
            # Combine context and user message
            full_prompt = f"Previous Context: {context}\n\nUser Message: {user_message}"
            
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": """You are EmoCare, an empathetic AI wellness assistant. 
                        Provide supportive, understanding responses that help users 
                        with their emotional well-being. Be kind, non-judgmental, 
                        and offer constructive advice."""
                    },
                    {
                        "role": "user",
                        "content": full_prompt
                    }
                ],
                model=self.model,
                temperature=0.7,
                max_tokens=300
            )
            
            response = chat_completion.choices[0].message.content
            logger.info("Response generated successfully")
            return response
        except Exception as e:
            logger.error(f"Response generation error: {e}")
            return f"I'm experiencing some difficulties. {str(e)}"