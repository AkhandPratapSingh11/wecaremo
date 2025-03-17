import os
import sys
from groq import Groq
from dotenv import load_dotenv
import logging

from openai import api_key

class EmoCareModel:
    def __init__(self):
        # Specify the exact path to the .env file
        env_path = '/home/akhand/Desktop/New Folder 1/wecaremo/.env'
        
        try:
            # Load environment variables from the specific path
            load_dotenv(dotenv_path=env_path)
            
            # Get API key with more robust checking
            api_key = os.getenv('GROQ_API_KEY')
            
            # Comprehensive API key validation
            if not api_key:
                logging.error("GROQ_API_KEY is missing in .env file")
                raise ValueError("GROQ_API_KEY is missing. Please add your Groq API key to the .env file.")
            
            if len(api_key.strip()) < 10:
                raise ValueError("Invalid API key. Please check your Groq API key.")
            
            # Initialize Groq client
            self.client = Groq(api_key=api_key)
            self.model = "qwen-2.5-32b"
            
            logging.info("EmoCare Model initialized successfully")
        except Exception as e:
            logging.error(f"Model initialization error: {e}")
            # Provide more detailed error information
            print(f"Error Details: {e}")
            print(f"Environment Path: {env_path}")
            print(f"Current Working Directory: {os.getcwd()}")
            print(f"Python Path: {sys.path}")
            raise


    def generate_response(self, context, user_message):
        """
        Generate empathetic response using Groq Qwen model with conversation context
        """
        try:
            # Prepare a comprehensive prompt with context
            full_prompt = f"""Conversation Context:{context} Latest User Message: {user_message} 
                               Please provide a thoughtful, empathetic, and contextually relevant response."""
            
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": """You are EmoCare, an empathetic AI wellness assistant. 
                        Provide supportive, understanding responses that help users 
                        with their emotional well-being. Be kind, non-judgmental, 
                        and offer constructive advice. Maintain context of the conversation 
                        and provide personalized support."""
                    },
                    {
                        "role": "user",
                        "content": full_prompt
                    }
                ],
                model=self.model,
                temperature=0.5,
                max_tokens=300
            )
            
            response = chat_completion.choices[0].message.content
            logging.info("Response generated successfully")
            return response
        except Exception as e:
            logging.error(f"Response generation error: {e}")
            return f"I'm experiencing some difficulties understanding the context. {str(e)}"