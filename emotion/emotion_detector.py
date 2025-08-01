# emotion/emotion_detector.py

"""
This module provides a modular and extensible interface for detecting emotions from images
using the FER (Facial Expression Recognition) library. It is designed to support future
enhancements such as batch processing and model switching.
"""

from fer import FER
import cv2

class EmotionDetector:
    """
    A class-based wrapper around the FER emotion detection model.
    """

    def __init__(self, use_mtcnn=True):
        """
        Initializes the emotion detector.

        Parameters:
        - use_mtcnn (bool): Whether to use MTCNN for face detection (default: True).
        """
        self.detector = FER(mtcnn=use_mtcnn)

    def detect_top_emotion(self, image):
        """
        Detects the top emotion from a single image.

        Parameters:
        - image (np.ndarray): The input image in OpenCV format.

        Returns:
        - tuple: (emotion label, confidence score) or (None, None) if no face is detected.
        """
        emotion, score = self.detector.top_emotion(image)
        return emotion, score

    def detect_all_emotions(self, image):
        """
        Detects all emotions and their confidence scores from a single image.

        Parameters:
        - image (np.ndarray): The input image in OpenCV format.

        Returns:
        - list: A list of dictionaries with bounding boxes and emotion scores.
        """
        return self.detector.detect_emotions(image)

# Example usage:
# detector = EmotionDetector()
# emotion, score = detector.detect_top_emotion(image)
# all_emotions = detector.detect_all_emotions(image)
