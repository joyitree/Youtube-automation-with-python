import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import pywhatkit     # it is used to play youtube video here.

chrome = webbrowser.Chrome(r"c:\Program Files (x86)\Google\Chrome\Application\new_chrome.exe")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def youtube():
    speak("welcome to youtube.")
    speak("what do you want? manual or need my help?")
    speak("if you need my help just say it..")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening........")
        r.energy_threshold = 500
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("recognizing......")
        query=r.recognize_google(audio, language="en-IN")
        if 'manual' in query:
            chrome.open("www.youtube.com")
            return
        else:
            print("recognizing......")
            query1=r.recognize_google(audio, language="en-IN")
            print(f"searching youtube:- {query1}\n")
            time.sleep(5)
            pywhatkit.playonyt(query1)

    except Exception as e:
        #print(e)
        print("sorry")
        speak("sorry I can't understand")
        
if __name__ == "__main__":
    youtube()