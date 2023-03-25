import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():


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

def Pass(pass_inp):
    password = "python"
    passss = str(password)
    
    if passss==str(pass_inp):
        speak("Access Granted.")
        import main
    else:
        speak("Invalid Password")
        
if __name__ == "__main__" :
    speak("This particular file is protected.")
    speak("Kindly provide the password to access.")
    passssssss = input("Enter the password : ")
    print(passssssss)
    Pass(passssssss)
    