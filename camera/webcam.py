# camera/webcam.py
import cv2


# camera/webcam.py
import cv2

def capture_face():
    image_path = "sample_image.jpg"  # Replace with your image path
    face_img = cv2.imread(image_path)

    if face_img is None:
        raise FileNotFoundError(f"Could not load image from {image_path}")

    return face_img

# def capture_face():
    cap = cv2.VideoCapture(0)
    print("Press 'q' to capture face and exit.")
    face_img = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Webcam - Press 'q' to capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            face_img = frame
            break

    cap.release()
    cv2.destroyAllWindows()
    return face_img
