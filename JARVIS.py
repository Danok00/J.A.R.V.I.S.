import os

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