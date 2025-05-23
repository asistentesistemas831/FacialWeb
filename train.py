import cv2
import numpy as np
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), 'uploads')
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modeloLBPHFace.xml')

def train_model():
    labels = []
    faces_data = []
    label = 0

    for name in os.listdir(DATA_PATH):
        person_path = os.path.join(DATA_PATH, name)
        if not os.path.isdir(person_path):
            continue
        for file in os.listdir(person_path):
            img_path = os.path.join(person_path, file)
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if image is not None:
                faces_data.append(image)
                labels.append(label)
        label += 1

    if not faces_data:
        print("No hay datos para entrenar.")
        return

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces_data, np.array(labels))
    face_recognizer.save(MODEL_PATH)
    print("Modelo entrenado y guardado en", MODEL_PATH)
