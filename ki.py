#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib, ssl
import time
import google
import urllib

from googlesearch import search
from gtts import gTTS
from time import ctime


#definitions:
def speak(audioString):
    #speechrecognition
    print(audioString)
    tts = gTTS(text=audioString, lang='de')
    tts.save("spoken.mp3")
    os.system("mpg321 spoken.mp3")


def wishMe():
    #greeting function
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       tts = gTTS("Good Morning Ben!")
       tts.save("spoken.mp3")
       os.system("mpg321 spoken.mp3")

    elif hour>=12 and hour<18:
        tts = gTTS("Good Afternoon Ben!")
        tts.save("spoken.mp3")
        os.system("mpg321 spoken.mp3")

    else:
        tts = gTTS("Good Evening Ben!")
        tts.save("spoken.mp3")
        os.system("mpg321 spoken.mp3")
        
    tts = gTTS("Please tell me how i may help you")       
    tts.save("spoken.mp3")
    os.system("mpg321 spoken.mp3")


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recognizing...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Working...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    #sends email from/to !pre-defined! adresses
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('example@gmail.com', 'passwd')
    server.sendmail('example@gmail.com', to, content)
    server.close()



def googleSearch(results):
    #performs google search
    query = takeCommand()
    
    for results in search(query, tld='com', num=10, stop=5, pause=2):
        tts = gTTS("on google i found:" + results)
        tts.save("googleResults.mp3")
        os.system("mpg321 googleResults.mp3")
        print(results)


#Main Program
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing wiki search tasks based on query
        if 'wikipedia' in query:
            tts = gTTS('Searching on Wiki')
            tts.save("spoken.mp3")
            os.system("mpg321 spoken.mp3")

            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print(results)
        
            tss = gTTS("On Wikipedia i found:" + results)
            tss.save("wikiResults.mp3")
            os.system("mpg321 wikiResults.mp3")

        #Logic for executing google search tasks based on query
        elif 'google search' in query:
            tts = gTTS("What would you like to search?")
            tts.save("spoken.mp3")
            os.system("mpg321 spoken.mp3")
            googleSearch(results=googleSearch)

        elif 'open google' in query:
            webbrowser.open_new_tab("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")   


        elif 'play music' in query:
            music_dir = "/System/Applications/Music.app/Contents/MacOS/Music"
            os.system(music_dir)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            tss = gTTS(f"Sir, the time is {strTime}")
            tss.save("spoken.mp3")
            os.system("mpg321 spoken.mp3")

        elif 'open code' in query:
            tts =gTTS("Open Visual Studio Code Application!")
            tts.save("spoken.mp3")
            os.system("mpg321 spoken.mp3")

            codePath = r"/Applications/Visual\ Studio\ Code.app"
            os.system(codePath)

        elif 'send mail office' in query:
            try:
                tss = gTTS("What should I write?")
                tss.save("spoken.mp3")
                os.system("mpg321 spoken.mp3")
                content = takeCommand()
                to = "info@bittec.ch"    
                sendEmail(to, content)
                tss = gTTS("Email has been sent!")
                tss.save("spoken.mp3")
                os.system("mpg321 spoken.mp3")
            
            except Exception as e:
                print(e)
                tss = gTTS("I'm not able to send your email")
                tss.save("spoken.mp3")
                os.system("mpg321 spoken.mp3")
