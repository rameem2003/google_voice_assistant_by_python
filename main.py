# Package import

# Package for recognition
import speech_recognition as sr

# Package for audio to text
import pyttsx3

# Package for date-time
import datetime

# Package for song
import pywhatkit

# for wikipidia
import wikipedia


listener = sr.Recognizer()
google = pyttsx3.init()
voices = google.getProperty('voices')
google.setProperty('voice', voices[1].id)


def talk(text):
    google.say(text)
    google.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("I am listening......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'google' in command:
                command = command.replace('google', '')
                print(command)
    except:
        pass
    return command


def run_google():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is" + time + " Thank you")

    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command:
        about = command.replace('tell me about', '')
        info = wikipedia.summary(about, 3)
        talk(info)




run_google()
