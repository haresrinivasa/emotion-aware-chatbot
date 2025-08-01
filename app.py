from flask import Flask, request, jsonify, send_from_directory, render_template
from backend.integration import process_image_from_frontend
import os

app = Flask(__name__, static_folder='docs', template_folder='docs')

# Serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Serve static files (JS, CSS)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Handle emotion detection POST request
@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    base64_image = data.get('image')
    result = process_image_from_frontend(base64_image)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
