# ZENO.V
A Basic Personal AI assistant with face recognition.
This assistant has a secure accessing using face recognition model making only authorized to access the assistant.  
## __Steps to run__  
__Step1-Run sample.py file__  
&nbsp;&nbsp;&nbsp;-this is a python file that is used to create face samples of the person who will acccess the assistant.  
&nbsp;&nbsp;&nbsp;-this file uses OpenCV to video capture from webcam and perform face detection using Haar Cascade Classifiers and save the images.Python &nbsp;&nbsp;&nbsp;Os is used to file handling,creating directories and&nbsp;&nbsp;&nbsp;constructing file path to store samples.  
&nbsp;&nbsp;&nbsp;-goal is to create samples for later use in training.  
__Step2-Run modeltrainer.py__  
&nbsp;&nbsp;&nbsp;-this is a second file you will run after generating samples this is where the samples get trained for a particular id.  
&nbsp;&nbsp;&nbsp;-it uses OpenCV for face detection,Local Binary Patterns Histograms(LBPH) for face recognition tasks,Pillow(PIL) for handling images and &nbsp;&nbsp;&nbsp;conversion to grayscale,Numpy for converting images in numpy arrays for efficient processing, again os module for organizing image &nbsp;&nbsp;&nbsp;samples and saves the trained model as a YAML file.  
__Step3-Run personal.py__  
&nbsp;&nbsp;&nbsp;-this file uses a wide range of AI technologies Pyttsx3 for text-to-speech conversion,Speech recognition for speech-to-text conversion and it &nbsp;&nbsp;&nbsp;first verifies the user using LBPH algorithm and &nbsp;&nbsp;&nbsp;many other modules to do various task like opening application,playing music,sending &nbsp;&nbsp;&nbsp;emails,speed test and many other.  
__Note__: there is another file facerecogn which need not be run separately but it always better to have a separte file.  
## __Conclusion__  
__ this was my first academic project as a team.As mentioned this is a basic model with basic functions also this model can be always improved in many ways especially in automation.__  
## __Acknowledgments__  
-this is a collaborative effort,with equal contributions from my fellow contributors  
--**[Abin Aiyspps MV]**:[Co-developer]  
&nbsp;&nbsp;&nbsp;--Github: [https://github.com/AbinAiyappaMV29]  
--**[Gopal Kattimani]**:[Co-developer]  
&nbsp;&nbsp;&nbsp;--Github: [(https://github.com/Gopalkattiamni)]  
--**[S Deva Dharshan]**:[Co-developer]  
&nbsp;&nbsp;&nbsp;--Github: [https://github.com/devadharshan07]  
 __NOTE:-__ _FOR ANY FURTHUR QUERIES, FEEDBACK OR CONTRIBUTIONS, CONTACT ME AT [koushik.murthy03@gmail.com]

