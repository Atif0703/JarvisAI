import speech_recognition as sr
import os
import webbrowser
import datetime

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 1
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error occured. Sorry from Jarvis"

if __name__ =='__main__':
    print('PyCharm')
    say("Hello I am Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites=[["youtube", "https//www.youtube.com"], ["wikipedia","https://www.wikipedia.com"],
               ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir")
                webbrowser.open(site[1])
        if "the time" in query:
            strfTime= datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time s {strfTime}")
        



