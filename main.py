import speech_recognition as sr 
import webbrowser
import pyttsx3

recogniser = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Speak the welcome message
    print("Hello, I am Ana. How can I assist you today?")
    speak("Hello, I am Ana. How can I assist you today?")
    
    # Recognize speech using Google Speech Recognition
    try:
        # Recognize listening Ana
        with sr.Microphone() as source:
            print("Listening...")
            audio = recogniser.listen(source)
        print("Recognizing...")
        command = recogniser.recognize_google(audio, language='en-US')
        print(f"You said: {command}")

        # Open a web browser with the command
        if command.lower() == "open google":
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        elif command.lower() == "open youtube":
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        else:
            speak("Command not recognized. Please try again.")
    
    except sr.UnknownValueError:
        print(f"You said: {command}")
        print("Sorry, I did not understand that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")