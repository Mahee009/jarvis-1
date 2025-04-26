import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(command):
    print(F"Command received: {command}")
    if "open google" in command.lower() :
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in command.lower() :
        webbrowser.open("https://www.youtube.com")
        speak("Opening Youtube")
    elif c.lower().startswith("play"):
        song =  command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        # let openai handle the request
        pass
        

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True: 
        #Listen for the wake word "Jarvis"

        #obtain audio from the microphone
        r = sr.Recognizer()
        #recognize speech using Google recognition
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                print("Audio captured")
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Ya")
                    # Listen for the command
                    with sr.Microphone() as source:
                        print("Jarvis Active..")
                        audio = r.listen(source, timeout=5)
                        command = r.recognize_google(audio)
                        processcommand(command)
        except Exception as e:
            print("Error: {0}".format(e))
        
            

        

