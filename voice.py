import pyttsx3

engine = pyttsx3.init("nsss")
voices = engine.getProperty("voices")

# for voice in voices:
#     print('-----------')
#     print(f'Name: {voice.name}')
#     print(f'ID: {voice.id}')
#     print(f'Language: {voice.languages}')
#     print(f'Gender: {voice.gender}')
#     print(f'Age: {voice.age}')

engine.setProperty('voice', 'eng')

for voice in voices:
    if voice.name == 'Milena':
        engine.setProperty('voice', voice.id)

rate = engine.setProperty('rate')
engine.setProperty('rate', rate-40)
engine.say('Hello')
engine.runAndWait()



