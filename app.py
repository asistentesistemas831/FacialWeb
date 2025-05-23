from flask import Flask, request, jsonify
from recognizer import recognize_face
from train import train_model
import os
import cv2

app = Flask(__name__)
UPLOAD_FOLDER = 'backend/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)

    name, confidence = recognize_face(path)
    return jsonify({'name': name, 'confidence': confidence})

@app.route('/train', methods=['POST'])
def train():
    train_model()
    return jsonify({'message': 'Modelo entrenado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)
