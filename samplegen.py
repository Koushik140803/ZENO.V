import cv2
import os

# Define the path to the 'samples' directory within the project folder
project_path = r'C:\Users\Kaushik\Desktop\New folder (2)\ZENO.V'
samples_dir = os.path.join(project_path, 'samples')

# Create a video capture object to capture video through the webcam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)  # Set video frame width
cam.set(4, 480)  # Set video frame height

# Ensure the 'samples' directory exists
if not os.path.exists(samples_dir):
    os.makedirs(samples_dir)

# Load the Haar Cascade Classifier for face detection
detector_path = os.path.join(project_path, 'cascades', 'haarcascade_frontalface_default.xml')
detector = cv2.CascadeClassifier(detector_path)

# Ask for a numeric user ID
face_id = input("Enter a Numeric user ID here: ")

print("Taking samples, look at the camera...")

count = 0  # Initializing sample face count

while True:
    ret, img = cam.read()  # Read frames using the video capture object
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a rectangle around the face
        count += 1

        # Save the captured image into the 'samples' directory
        try:
            file_path = os.path.join(samples_dir, f"face.{str(face_id)}.{str(count)}.jpg")
            cv2.imwrite(file_path, converted_image[y:y+h, x:x+w])
            print(f"Saved: {file_path}")
        except Exception as e:
            print(f"Error saving image: {e}")

        cv2.imshow('image', img)  # Display the image in a window

    k = cv2.waitKey(100) & 0xff  # Wait for a pressed key
    if k == 27:  # Press 'ESC' to stop
        break
    elif count >= 10:  # Take 10 samples (you can increase for more accuracy)
        break

print("Samples taken, now closing the program...")
cam.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows
1