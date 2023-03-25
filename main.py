import subprocess
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pyjokes
import winshell
import shutil
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir ! , सुप्रभात सर")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir ! ,नमस्कार")

	else:
         speak("Good Evening Sir !, शुभ संध्या")
        
         speak("Hello sir. How may I help you , नमस्ते महोदय। कृपया मुझे बताएं कि मैं आपकी कैसे मदद कर सकता हूं")

def username():
    speak("What should i call you sir, मैं आपको क्या कहूं सर")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("*********************************".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("*********************************".center(columns))

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

if __name__ == "__main__":
    wishMe()
    username()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            speak("Here you go to youtube")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Here you go to google")
            webbrowser.open("https://www.google.com/")
        
        elif 'open spotify' in query:
            speak("Here you go to Spotify for some entertainment")
            webbrowser.open("https://open.spotify.com/")

        elif 'open latest news' in query:
            speak("Here are some latest news")
            webbrowser.open("https://www.hindustantimes.com/")

        elif 'open cricbuzz ' in query:
            webbrowser.open("https://www.cricbuzz.com/")

        elif 'open weather' in query:
            webbrowser.open("https://www.accuweather.com/en/in/kota/190216/weather-forecast/190216")

        elif 'open calendar' in query:
            webbrowser.open("https://www.timeanddate.com/calendar/")

        elif 'open calculator' in query:
            webbrowser.open("https://www.calculator.net/")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir , आप कैसे हो सर ")

        elif 'fine' in query or "good " in query:
            speak("It's good to know that your fine ,यह जानकर अच्छा लगा कि आप ठीक हैं")

        elif 'exit' in query:
            speak("Thanks for giving me your time , मुझे अपना समय देने के लिए धन्यवाद")
            exit()
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\hp\\Downloads\\Spotify Clone\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'clear recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        elif 'play movie' in query:
            movie_dir = 'D:\\Movie'
            movie = os.listdir(movie_dir)
            print(movie)    
            os.startfile(os.path.join(movie_dir, movie[0]))

        elif "why you came to world" in query:
            speak("Thanks to You. further It's a secret ,आपका धन्यवाद। आगे यह एक रहस्य है ")

        elif 'game setup' in query:
            game_dir = 'D:\\Game setup'
            game = os.listdir(game_dir)
            print(game)    
            os.startfile(os.path.join(game_dir, game[0]))

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps" + location + "")
        
        elif 'open presentation' in query:
            codePath = "D:\\ppt\\Desktop Assistant.pptx"
            os.startfile(codePath)
        
        elif 'whats the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'restart' in query:
            subprocess.call(["shutdown", "/r"])

        elif 'open career point university website' in query:
            speak("Here you go to CPU KOTA website")
            webbrowser.open("https://cpukota.mastersofterp.in/iitmsv4eGq0RuNHb0G5WbhLmTKLmTO7YBcJ4RHuXxCNPvuIw=?enc=EGbCGWnlHNJ/WdgJnKH8DA==")

takeCommand() 
