# ZENO.V
A Basic Personal AI assistant with face recognition.
This assistant has a secure accessing using face recognition model making only authorized to access the assistant.  
__Steps to run__  
__Step1-Run sample.py file__  
-this is a python file that is used to create face samples of the person who will acccess the assistant.  
-this file uses OpenCV to video capture from webcam and perform face detection using Haar Cascade Classifiers and save the images.Python Os is used to file handling,creating directories and constructing file path to store samples.  
-goal is to create samples for later use in training.  
__Step2-Run modeltrainer.py__  
-this is a second file you will run after generating samples this is where the samples get trained for a particular id.  
-it uses OpenCV for face detection,Local Binary Patterns Histograms(LBPH) for face recognition tasks,Pillow(PIL) for handling images and conversion to grayscale,Numpy for converting images in numpy arrays for efficient processing, again os module for organizing image samples and saves the trained model as a YAML file.  
__Step3-Run personal.py__
-this file uses a wide range of AI technologies Pyttsx3 for text-to-speech conversion,Speech recognition for speech-to-text conversion and it first verifies the user using LBPH algorithm and many other modules to do various task like opening application,playing music,sending emails,speed test and many other.  
__Note__: there is another file facerecogn which need not be run separately but it always better to have a separte file.  
__Conclusion__ :  
__As mentioned this is a basic model with basic functions also this model can be always improved in many ways that is the reason this was the first project as a team.__  
__Acknowledgments__:  
-this is a collaborative effort, and these are my fellow contributors  
--**[Abin Aiyspps MV]**:[Co-developer]  
 --Github: [https://github.com/AbinAiyappaMV29]  
--**[S Deva Dharshan]**:[Co-developer]  
 --Github: [https://github.com/devadharshan07]  
 __For any queries or contributions can contant me at [koushik.murthy03@gmail.com]__  
