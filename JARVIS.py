import os
import speech_recognition as sr

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


command()