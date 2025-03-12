class ConversationMemory:
    """
    Manages conversation history for context-aware AI responses.
    Stores user and AI messages in a session-like format.
    """

    def __init__(self):
        """Initializes an empty conversation history."""
        self.chat_history = []

    def save_message(self, role: str, content: str):
        """
        Saves a message to the conversation history.
        
        Args:
            role (str): Role of the message sender ("User" or "AI").
            content (str): The message content.
        """
        self.chat_history.append({"role": role, "content": content})

        # Maintain only the last 10 exchanges for efficiency
        if len(self.chat_history) > 20:
            self.chat_history.pop(0)

    def get_chat_history(self):
        """
        Retrieves the chat history.
        
        Returns:
            list: List of past user and AI messages.
        """
        return self.chat_history

    def clear_memory(self):
        """Clears the conversation history."""
        self.chat_history = []
