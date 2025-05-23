import cv2
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), 'uploads')
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modeloLBPHFace.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(MODEL_PATH)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def recognize_face(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return 'No se detectó rostro', None

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (150, 150))
        label, confidence = face_recognizer.predict(face)
        people = os.listdir(DATA_PATH)
        name = people[label] if label < len(people) else 'Desconocido'
        return name, round(confidence, 2)

    return 'No se pudo reconocer', None
