import pyttsx3
import speech_recognition as sr
import datetime 
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import psutil
import speedtest
from FaceRecog import recognize_face  # Import the face recognition function

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)

# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Voice into text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            speak("I didn't hear you. Please try again.")
            return "none"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("Could you say that again, please?")
        return "none"
    return query.lower()

# To wish the user
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. Before I help you, I need to know it's you.")

# To send email
def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_id', 'your_password')
    server.sendmail('your_email_id', to, content)
    server.close()

# Command Functions
def open_notepad():
    npath = "C:\\Windows\\SysWOW64\\notepad.exe"
    os.startfile(npath)

def open_cmd():
    os.system("start cmd")

def open_camera():
    cap = cv2.VideoCapture(1)
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam', img)
        k = cv2.waitKey(50)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def play_music():
    music_dir = "C:\\songs music"
    songs = os.listdir(music_dir)
    for song in songs:
        if song.endswith('.mp3'):
            os.startfile(os.path.join(music_dir, song))

def get_ip():
    ip = get('https://api.ipify.org').text
    speak(f"Your IP address is {ip}")

def search_wikipedia(query):
    speak("Searching Wikipedia...")
    results = wikipedia.summary(query, sentences=2)
    speak(results)
    print(results)

def open_youtube():
    webbrowser.open("www.youtube.com")

def open_instagram():
    webbrowser.open("www.instagram.com")

def open_stackoverflow():
    webbrowser.open("www.stackoverflow.com")

def open_google():
    speak("What should I search on Google?")
    cm = take_command().lower()
    webbrowser.open(f"{cm}")

def play_youtube_song():
    cm = take_command().lower()
    kit.playonyt(cm)

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def close_notepad():
    speak("Okay, closing Notepad.")
    os.system("taskkill /f /im notepad.exe")

def shutdown():
    os.system("shutdown /s /t 5")

def restart():
    os.system("shutdown /r /t 5")

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def check_battery():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Our system has {percentage} percent battery")
    if percentage >= 75:
        speak("We have enough power to continue working.")
    elif 40 <= percentage < 75:
        speak("We should connect our system to the charging point.")
    elif 15 <= percentage < 40:
        speak("We don't have enough power to work, please connect to charging.")
    else:
        speak("We have very low power, the system will shut down soon.")

def check_internet_speed():
    st = speedtest.Speedtest()
    dl = st.download()
    up = st.upload()
    speak(f"Our internet speed is {dl:.2f} bps download and {up:.2f} bps upload.")

# Command Dictionary
command_dict = {
    "open notepad": open_notepad,
    "open command prompt": open_cmd,
    "open camera": open_camera,
    "play music": play_music,
    "ip address": get_ip,
    "wikipedia": search_wikipedia,
    "open youtube": open_youtube,
    "open instagram": open_instagram,
    "open stackoverflow": open_stackoverflow,
    "open google": open_google,
    "play song on youtube": play_youtube_song,
    "tell me a joke": tell_joke,
    "close notepad": close_notepad,
    "shut down": shutdown,
    "restart": restart,
    "sleep": sleep,
    "how much power left": check_battery,
    "battery": check_battery,
    "internet speed": check_internet_speed,
}

# Ask for user ID and verify using face recognition
def verify_user():
    speak("Please type your ID number.")
    user_id = input("Enter your ID number: ")  # Use input() to get the ID from the user
    if recognize_face(user_id):
        speak(f"Access granted for User ID {user_id}.")
        return True
    else:
        speak("Access denied. Face recognition failed.")
        return False

if __name__ == "__main__":
    wish()
    if verify_user():
        while True:
            query = take_command()

            # Check if query matches any command
            for command, function in command_dict.items():
                if command in query:
                    function()
                    break
            else:
                speak("Sorry, I did not understand that command.")
