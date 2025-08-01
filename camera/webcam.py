#camera/webcam.py

import cv2
import numpy as np
import base64

def decode_base64_image(base64_string):
    """
    Decodes a base64-encoded image string (from browser webcam) into an OpenCV image (NumPy array).

    Parameters:
    - base64_string (str): The base64-encoded image string from the frontend.

    Returns:
    - image (np.ndarray): The decoded image in OpenCV format.
    """
    try:
        # Remove data URL prefix if present (e.g., "data:image/jpeg;base64,...")
        if "," in base64_string:
            base64_string = base64_string.split(",")[1]

        # Decode the base64 string into bytes
        image_bytes = base64.b64decode(base64_string)

        # Convert bytes to a NumPy array
        np_array = np.frombuffer(image_bytes, np.uint8)

        # Decode the image using OpenCV
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError("Failed to decode image from base64 string.")

        return image

    except Exception as e:
        raise ValueError(f"Error decoding base64 image: {e}")
