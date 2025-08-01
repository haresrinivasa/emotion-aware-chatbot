#chatbot/empathetic_bot.py

"""
This module provides a modular and extensible framework for generating empathetic chatbot responses
based on detected emotions. It is designed to support future enhancements such as multilingual support
and emotion intensity scaling.
"""

# Dictionary mapping emotions to default English responses
DEFAULT_RESPONSES_EN = {
    "happy": "I'm glad to see you're happy! 😊",
    "sad": "I'm here for you. Want to talk about it?",
    "angry": "Take a deep breath. I'm here to help.",
    "surprise": "Wow! That sounds exciting!",
    "neutral": "How can I assist you today?",
    "disgust": "I'm sorry you're feeling that way.",
    "fear": "You're not alone. I'm here with you."
}

def get_response_by_emotion(emotion, language="en", intensity=None):
    """
    Generates a chatbot response based on the detected emotion.

    Parameters:
    - emotion (str): The detected emotion (e.g., "happy", "sad").
    - language (str): Language code for the response (default is "en").
    - intensity (float or None): Optional emotion intensity for future scaling.

    Returns:
    - str: An empathetic response string.
    """

    # Future enhancement: Add multilingual support
    if language == "en":
        responses = DEFAULT_RESPONSES_EN
    else:
        # Placeholder for other languages
        responses = DEFAULT_RESPONSES_EN  # fallback to English

    # Future enhancement: Adjust response based on intensity
    # For now, intensity is not used

    # Return the response or a default fallback
    return responses.get(emotion, "I'm here to chat whenever you're ready.")
