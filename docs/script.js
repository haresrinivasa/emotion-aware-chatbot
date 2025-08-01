// docs/Script.js

// Handles webcam access, image capture, and communication with the backend.

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureBtn = document.getElementById('captureBtn');
const emotionSpan = document.getElementById('emotion');
const confidenceSpan = document.getElementById('confidence');
const responseSpan = document.getElementById('response');

// Access webcam
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Error accessing webcam:", err);
    });

// Capture frame and send to backend
captureBtn.addEventListener('click', () => {
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const base64Image = canvas.toDataURL('image/jpeg');

    fetch('/detect_emotion', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: base64Image })
    })
    .then(response => response.json())
    .then(data => {
        emotionSpan.textContent = data.emotion || "N/A";
        confidenceSpan.textContent = data.confidence !== null ? data.confidence + "%" : "N/A";
        responseSpan.textContent = data.response || "No response.";
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
