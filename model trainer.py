import cv2
import numpy as np
from PIL import Image
import os

# Define the project path and relevant directories
project_path = r'C:\Users\Kaushik\Desktop\New folder (2)\ZENO.V'
samples_dir = os.path.join(project_path, 'samples')
cascade_path = os.path.join(project_path, 'cascades', 'haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cascade_path)

def Images_And_Labels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
        img_numpy = np.array(PIL_img, 'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids

print("Training faces. It will take a few seconds. Wait ...")

faces, ids = Images_And_Labels(samples_dir)
recognizer.train(faces, np.array(ids))

# Save the model into the trainer directory
trainer_dir = os.path.join(project_path, 'trainer')
if not os.path.exists(trainer_dir):
    os.makedirs(trainer_dir)

recognizer.write(os.path.join(trainer_dir, 'trainer.yml'))  # Save the trained model as trainer.yml

print(f"{len(np.unique(ids))} faces trained. Exiting Program...")
