from typing import Text
import speech_recognition 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take():
    try:
        with speech_recognition.Microphone() as source:
            print('listenning....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'bot' in command:
                print(command)
    except:
        pass
    return command

def run():
    command=take()
    print (command)
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('yes playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Curent time is ' + time)

    elif 'what is' in command:
        person = command.replace('what is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    elif 'who is' in command:
        person2 = command.replace('who is ', '')
        info = wikipedia.summary(person2, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    #elif "exit" in command:
        
        #print(choice)
        #talk('ok thank you')           
    else:
        talk('sorry i did not heard you...')


#choice = " "
#while choice !="exit":

while True:
    run()


    

