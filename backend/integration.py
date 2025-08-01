# backend/integration.py

import os
import sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # Suppress TensorFlow warnings
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tensorflow as tf
import logging
tf.get_logger().setLevel(logging.ERROR)

from camera.webcam import decode_base64_image
from emotion.emotion_detector import EmotionDetector
from chatbot.empathetic_bot import get_response_by_emotion

# Initialize the emotion detector once
emotion_detector = EmotionDetector()

def process_image_from_frontend(base64_image):
    """
    Main entry point for web-based emotion detection and response generation.

    Parameters:
    - base64_image (str): Base64-encoded image string from the frontend.

    Returns:
    - dict: Contains emotion, confidence score, and chatbot response.
    """
    try:
        # Decode the image from base64
        image = decode_base64_image(base64_image)

        # Detect emotion
        emotion, score = emotion_detector.detect_top_emotion(image)

        # Generate chatbot response
        response = get_response_by_emotion(emotion)

        return {
            "emotion": emotion,
            "confidence": round(score * 100, 1) if score else None,
            "response": response
        }

    except Exception as e:
        return {
            "error": str(e),
            "emotion": None,
            "confidence": None,
            "response": "Sorry, something went wrong while processing the image."
        }
