# import library used 
from email.mime import audio
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import time
import os
import random
from time import ctime


r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source :
        if ask :
            bot_ahmed(ask)
        audio = r.listen(source)
        voice_data =''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            bot_ahmed('Sorry, I did not get that')
        except sr.RequestError:
            bot_ahmed('Sorry, my speech service is down')
        return voice_data

def bot_ahmed(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond (voice_data):
    if 'what is your name' in voice_data:
        bot_ahmed('My name is Ahmed')
    if 'what time is it' in voice_data:
        bot_ahmed(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        bot_ahmed('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        bot_ahmed('Here is the location of ' + location)
    if 'hel google' in voice_data:
        webbrowser.get().open('https://google.com')
    
    if 'go to sleep' in voice_data:
        bot_ahmed('Goodbye')
        exit()
    if 'exit' in voice_data:
        bot_ahmed('bye')
        exit()

time.sleep(1)
bot_ahmed('How can I help you?')
while 1:
    voice_data = record_audio()
    bot_ahmed(voice_data)
