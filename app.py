# app.py
from camera.webcam import capture_face
from emotion.emotion_detector import detect_emotion
from chatbot.empathetic_bot import generate_response

def main():
    print("Starting Emotion-Aware Chatbot...")
    face_image = capture_face()
    emotion = detect_emotion(face_image)
    response = generate_response(emotion)
    print(f"Detected Emotion: {emotion}")
    print(f"Chatbot Response: {response}")

if __name__ == "__main__":
    main()
