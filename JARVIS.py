import os
import speech_recognition as sr
import webbrowser

#---------------
#import pyttsx3
#engine = pyttsx3.init()
#engine.say('Текст')
#engine.runAndWait()
#--------------

def talk(words):
    print(words)
    os.system('say ' + words)


talk('Привіт, як справи')
talk('Hello')



def command():
    r = sr.Recognizer

    with sr.Microphone() as source:
        print('Say')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    task = r.recognize_google(audio, language = 'en=US').lower()
    print('You: ' + task)

    return task



def make_something(ar_task):
    if ('open' and 'site') in ar_task:
        talk('ok')
        url = 'https://rezka.ag/films/'
        webbrowser.open(url)

while True:
    make_something(command())