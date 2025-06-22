import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)
recognizer = sr.Recognizer()
def cmd():
    with sr.Microphone() as source:
        print('clearing background noises..Please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything..')
        recordedaudio = recognizer.listen(source)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except sr.WaitTimeoutError:
                print("[DEBUG] No speech detected in time.")
                speak("You were quiet. Let’s try again.")
                return ""
            except sr.UnknownValueError:
                print("[DEBUG] Speech was unclear.")
                speak("Hmm, I didn’t catch that. Could you please repeat?")
                return ""
            except sr.RequestError:
                speak("Sorry, there's a network issue.")
                return ""
def respond(command):
    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time} now")
    elif "date" in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date}")
    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Here are the search results for {query}")
    elif "wikipedia" in command:
        speak("What should I search on Wikipedia?")
        query = listen()
        if query:
            summary = wikipedia.summary(query, sentences=2)
            speak(summary)
    else:
        speak("I'm not sure how to help with that yet.")
# Main Loop
speak("Hii,I am your Voice Assistant.")
while True:
    command = listen()
    if "stop" in command:
        speak("Okay bye, let's talk soon")
        break
    respond(command)
