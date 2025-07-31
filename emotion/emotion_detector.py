# emotion/emotion_detector.py
from fer import FER
import cv2

def detect_emotion(image):
    detector = FER(mtcnn=True)
    emotion, score = detector.top_emotion(image)
    return emotion, score
