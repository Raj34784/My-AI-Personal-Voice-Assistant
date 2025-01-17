
# First Install All The Dependencies By Running The Codes In Terminal

# Download PyAudio From This Link First According To Your Python Version Then Run pip with the Downloaded File Location
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Or I Have Uploaded The Present Latest .whl In This Repo Only.
# Just Download It To Your Preferred Location And Run The Below Command By Changing The Location.
# pip install 'c:\Users\Soumwadeep Guha\Documents\My Codes\PyAudio-0.2.11-cp39-cp39-win_amd64.whl'

# Created By Soumwadeep Guha.

import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import pyjokes
import os
import smtplib
import secrets
import random
from dotenv import load_dotenv

load_dotenv()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)  # smtp of your email provider
    server.ehlo()
    server.starttls()
    mail_address = os.getenv('MAIL_ADDRESS')
    mail_password = os.getenv('MAIL_PASSWORD')
    server.login(mail_address, mail_password)
    server.sendmail(mail_address, to, content)
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

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = os.getenv("MUSIC_DIR")
            print("[+] Searching:", music_dir)
            if os.path.isdir(music_dir):
                songs = [
                    file
                    for file in os.listdir(music_dir)
                    if file.endswith(".wav") or file.endswith(".mp3")
                ]
                if not songs:
                    speak("Sorry Sir, No valid songs found")
                    continue
                song = random.choice(songs)
                print("[+] Playing:", song)
                os.startfile(os.path.join(music_dir, song))
            else:
                speak("Sorry Sir, The Music Directory is not available")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "code"
            os.startfile(codePath)
        elif 'open word' in query:
            wordPath = "WINWORD"
            os.startfile(wordPath)
        elif 'open excel' in query:
            excelPath = "EXCEL"
            os.startfile(excelPath)
        elif 'open powerpoint' in query:
            powerpointPath = "POWERPNT"
            os.startfile(powerpointPath)

        elif 'email to sdg' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "soumwadeep@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        elif 'toss a coin' in query:
            coin = secrets.randbelow(1)
            if(coin == 1):
                speak("Heads")
            else:
                speak("Tails")
        elif 'joke' in query:
            joke = pyjokes.get_joke(language='en', category='neutral')
            print(joke)
            speak(joke)
        elif 'restart' in query:
            speak("Restarting System")
            os.system('shutdown -r')
            break
        elif 'shutdown' in query:
            speak("Shutting Down System")
            os.system('shutdown -s')
            break
        elif 'close' in query:
            speak("Thanks Sir, Have A Great Day")
            break
# Created By Soumwadeep Guha.
