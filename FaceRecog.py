import cv2
import os

# Assuming the cascade and trainer paths are correctly set
project_path = os.path.dirname(os.path.abspath(__file__))
cascade_path = os.path.join(project_path, 'cascades', 'haarcascade_frontalface_default.xml')
trainer_path = os.path.join(project_path, 'trainer', 'trainer.yml')

def recognize_face(expected_id):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(trainer_path)
    detector = cv2.CascadeClassifier(cascade_path)

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, img = cam.read()
    cam.release()

    if not ret:
        print("Failed to capture image.")
        return False

    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(converted_image[y:y+h, x:x+w])
        if confidence < 50 and str(id) == expected_id:
            return True

    return False
