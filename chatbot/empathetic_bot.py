# chatbot/empathetic_bot.py
def generate_response(emotion):
    responses = {
        "happy": "I'm glad to see you're happy! 😊",
        "sad": "I'm here for you. Want to talk about it?",
        "angry": "Take a deep breath. I'm here to help.",
        "surprise": "Wow! That sounds exciting!",
        "neutral": "How can I assist you today?",
        "disgust": "I'm sorry you're feeling that way.",
        "fear": "You're not alone. I'm here with you."
    }
    return responses.get(emotion, "I'm here to chat whenever you're ready.")
