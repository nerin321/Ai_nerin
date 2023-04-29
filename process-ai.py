import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from ai_gui1 import Ui_MainWindow

class Process(object):
    def __init__(self):
        path = ChromeDriverManager().install()
        self.translator = Translator()
    
#chuyen van ban thanh am thanh
    def speak(self, query):
        language = Ui_MainWindow.language_set()
        # print("Nerin: {}".format(text))
        Ui_MainWindow.chat_show.append("Nerin: {}".format(query))
        tts = gTTS(text=query, lang=language, slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3", False)
        os.remove("sound.mp3")

#chuyen am thanh sang van ban
    def get_audio(self):
        c = sr.Recognizer()
        with sr.Microphone() as source: 
            c.pause_threshold = 1
            audio = c.listen(source)
        try:
            text = c.recognize_google(audio,language ="vi-VN")
            print("Nerin: " + text)
        except sr.UnknownValueError:
            print(self.trans("vui lòng lặp lại hoặc gõ lệnh."))
        return text
# dịch 
    def trans(self, query):
        language = Ui_MainWindow.language_set()
        query =  self.translator.translate(query, src='vi', dest= language).text
        return query
        
    def stop(self):
        self.speak(self.trans("Hẹn gặp lại bạn sau!"))
    
    #chào hỏi
    def welcome(self):
        hour =  datetime.datetime.now().hour
        if hour >= 6 and hour< 12 :
            self.speak(self.trans("Chào buổi sáng"))
        elif hour >= 12 and hour < 18 :
            self.speak(self.trans("Chào buổi chiều"))
        elif hour >= 18 and hour <= 24 :
            self.speak(self.trans("Chào buổi tối"))
        time.sleep(1)
        self.speak(self.trans('Tôi có thể giúp gì cho bạn?'))