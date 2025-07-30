# 🤖 Emotion-Aware Chatbot

A real-time, webcam-integrated chatbot that detects human emotions using facial expressions 
and responds empathetically. This project combines computer vision, deep learning, and 
natural language processing to create a more emotionally intelligent conversational experience.

---

## 💡 Project Overview

This Emotion-Aware Chatbot captures a user's facial expression via webcam, detects their emotional state using a pre-trained deep learning model, and generates a contextually appropriate response. It's designed to demonstrate how AI can be used to build emotionally responsive systems, with potential applications in mental health support, customer service, and human-computer interaction.

---

## 🎯 Key Features

- 📷 **Webcam Integration**: Captures real-time facial images.
- 🤖 **Emotion Detection**: Uses the `FER` (Facial Expression Recognition) library with MTCNN for accurate emotion classification.
- 💬 **Empathetic Responses**: Generates human-like responses tailored to the detected emotion.
- 🧩 **Modular Design**: Clean separation of concerns across camera, emotion detection, and chatbot logic.

---

## 🛠️ Tech Stack

- **Language**: Python 3.11
- **Libraries**:
  - `OpenCV` – for webcam access and image capture
  - `FER` – for facial emotion recognition
  - `TensorFlow` – backend for emotion detection model
  - `Keras` – model loading and inference
- **Environment**: Virtualenv / VS Code Dev Container

---

## 🧠 How It Works
1. **Capture**: The webcam captures a live image when the user presses q.

2. **Detect**: The image is passed to the FER model to identify the dominant emotion.

3. **Respond**: A chatbot message is generated based on the detected emotion.

---

## 📌 Example Output
-- Starting Emotion-Aware Chatbot... 
-- Press 'q' to capture face and exit.
-- Detected Emotion: happy
-- Chatbot Response: I'm glad to see you're happy! 😊

---

## 📁 Project Structure
```
emotion-aware-chatbot/
├── ⚙️  .devcontainer/              # Development container setup for GitHub Codespaces or VS Code
│   └── 📄 devcontainer.json        # Configuration file defining the container environment
│
├── 📷  camera/                     # Webcam-related functionality
│   └── 📄 webcam.py                # Captures live video and extracts facial images
│
├── 💬  chatbot/                    # Chatbot logic and empathetic response generation
│   └── 📄 empathetic_bot.py        # Returns emotion-specific responses based on detected emotion
│
├── 😶  emotion/                    # Emotion detection logic
│   └── 📄 emotion_detector.py      # Uses FER to detect emotions from facial images
│
├── 🚀  app.py                      # Main application entry point that ties all modules together 
├── 📦  requirements.txt            # Python dependencies for the project
├── 🙈  .gitignore                  # Specifies files and folders to be ignored by Git
└── 📘  README.md                   # Project documentation (you are reading this now 😜)
```
---

## 🚀 Getting Started

### 1. Clone the Repository

`git clone https://github.com/haresrinivasa/emotion-aware-chatbot.git`

`cd emotion-aware-chatbot`

### 2. Setting up the Virtual Environment

`python -m venv first_build_env`

`source first_build_env/bin/activate  # On Windows: first_build_env\Scripts\activate`

### 3. Installing the Dependencies

`pip install -r requirements.txt`

### 4. Running the Application

`python app.py`

## 📫 Contact
balaji27venkatesh@gmail.com
