import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import playsound
import pygame
import random
import cv2
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(" Aii shukla Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\asbaa\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))



        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\asbaa\\Desktop\\VoiceAI\\main.py"
            os.startfile(codePath)

        elif 'sword art online' in query:
            speak('Playing sword art online')
            songs = (
                "C:\\Users\\asbaa\\Desktop\\songs\\Sword Art Online - Opening 6  4K  60FPS  Creditless.mp3",
                "C:\\Users\\asbaa\\Desktop\\songs\\Sword Art Online - Opening 7  4K  60FPS  Creditless.mp3",
                "C:\\Users\\asbaa\\Desktop\\songs\\Sword Art Online - Opening 9  4K  60FPS  Creditless.mp3",
                "C:\\Users\\asbaa\\Desktop\\songs\\Sword Art Online - Opening 1  4K  60FPS  Creditless.mp3",
                "C:\\Users\\asbaa\\Desktop\\songs\\Sword Art Online - Opening 3  4K  60FPS  Creditless.mp3"
            )
            selected = random.choice(songs)
            print(selected)

            pygame.mixer.init()
            pygame.mixer.music.load(selected)
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy() == True:
                pass



        elif 'email to asbaa' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "asbaa.thakur@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'farewell' in query:
            speak("Bye Thanks for using my services")
            False
        else:
            speak('I cant compute complex functions as i am still learning')