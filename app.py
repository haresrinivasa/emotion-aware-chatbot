# app.py

# code only to supress the warning
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress INFO, WARNING, and ERROR logs from TensorFlow
import tensorflow as tf
import logging
tf.get_logger().setLevel(logging.ERROR)


from camera.webcam import capture_face
from emotion.emotion_detector import detect_emotion
from chatbot.empathetic_bot import generate_response

def main():
    print("Starting Emotion-Aware Chatbot ...")
    face_image = capture_face()
    emotion, score = detect_emotion(face_image)
    response = generate_response(emotion)
    if emotion is None or score is None:
        print(f"Detected Emotion: {emotion}")
    else:
        print(f"Detected Emotion: {emotion} (Confidence: {score*100:.1f} %)")
    print(f"Chatbot Response: {response}")

if __name__ == "__main__":
    main()
