import os
import sys

import speech_recognition as sr
import webbrowser

import openai

from dotenv import load_dotenv as ld
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    ld(dotenv_path)

openai.api_key = os.getenv('api_key')

def ai_response(user_input):
    compiletion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': user_input}]
    )
    return compiletion

#---------------
#import pyttsx3
#engine = pyttsx3.init()
#engine.say('Текст')
#engine.runAndWait()
#--------------

def talk(words):
    print(words)
    os.system('say ' + words)


# talk('Привіт, як справи')
#talk('Hello')
talk('Привет')

r = sr.Recognizer()
def command():


    with sr.Microphone() as source:
        print('Say')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language = 'ru-RU').lower()
        #task = r.recognize_google(audio, language = 'en-US').lower()
        #task = r.recognize_google(audio, language='uk-UA').lower()
        print('You: ' + task)
    except sr.UnknownValueError:
        talk('Не понял тебя')
        task = command()

    return task



def make_something(ar_task):
    if ('открой' and 'сайт') in ar_task:
        talk('ok')
        url = 'https://rezka.ag/films/'
        webbrowser.open(url)

    elif 'стоп' in ar_task:
        talk('Пока')
        sys.exit()

    elif ('зовут' and 'тебя') in ar_task:
        talk('My name is JARVIS')

    else:
        # print(handle_input(input("You: ")).choices[0].message.content)
        try:
            ai_res = ai_response(ar_task).choices[0].message.content
            talk(ai_res)
        except openai.error.ServiceUnavailableError:
            talk("Появилась ошибка, попробуй еще раз")
            try:
                ai_res = ai_response(ar_task).choices[0].message.content
                talk(ai_res)
            except openai.error.ServiceUnavailableError:
                talk("Не могу обробатать ответ попробуй еще раз")
            except openai.error.RateLimitError:
                talk('Попробуй через 20 секунд')
                r.pause_threshold = 20
            except:
                talk('Упс, что-то пошло не так. Попробуй еще')




while True:
    make_something(command())