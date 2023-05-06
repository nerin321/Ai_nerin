# Form implementation generated from reading ui file 'ai_gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

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
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.translator = Translator()
        self.flag = None
        self.t=""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 760)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/assistant.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chat_show = QtWidgets.QTextBrowser(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.chat_show.setFont(font)
        self.chat_show.setObjectName("chat_show")
        self.verticalLayout_3.addWidget(self.chat_show)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(471, 141))
        self.stackedWidget.setMaximumSize(QtCore.QSize(471, 141))
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_box = QtWidgets.QWidget()
        self.main_box.setObjectName("main_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.keybord_btn = QtWidgets.QPushButton(parent=self.main_box)
        self.keybord_btn.setEnabled(True)
        self.keybord_btn.setMaximumSize(QtCore.QSize(111, 71))
        self.keybord_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.keybord_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/keyboard-svgrepo-com.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.keybord_btn.setIcon(icon1)
        self.keybord_btn.setIconSize(QtCore.QSize(60, 60))
        self.keybord_btn.setObjectName("keybord_btn")
        self.horizontalLayout.addWidget(self.keybord_btn)
        self.mic_btn = QtWidgets.QToolButton(parent=self.main_box)
        self.mic_btn.setMaximumSize(QtCore.QSize(111, 71))
        self.mic_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mic_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/mic.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.mic_btn.setIcon(icon2)
        self.mic_btn.setIconSize(QtCore.QSize(60, 60))
        self.mic_btn.setObjectName("mic_btn")
        self.horizontalLayout.addWidget(self.mic_btn)
        self.setting_btn = QtWidgets.QPushButton(parent=self.main_box)
        self.setting_btn.setMaximumSize(QtCore.QSize(121, 71))
        self.setting_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.setting_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setting_btn.setIcon(icon3)
        self.setting_btn.setIconSize(QtCore.QSize(60, 60))
        self.setting_btn.setObjectName("setting_btn")
        self.horizontalLayout.addWidget(self.setting_btn)
        self.stackedWidget.addWidget(self.main_box)
        self.send_mess = QtWidgets.QWidget()
        self.send_mess.setObjectName("send_mess")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.send_mess)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.text_query = QtWidgets.QLineEdit(parent=self.send_mess)
        self.text_query.setMinimumSize(QtCore.QSize(331, 41))
        self.text_query.setMaximumSize(QtCore.QSize(331, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.text_query.setFont(font)
        self.text_query.setObjectName("text_query")
        self.horizontalLayout_2.addWidget(self.text_query)
        self.send_btn = QtWidgets.QPushButton(parent=self.send_mess)
        self.send_btn.setMaximumSize(QtCore.QSize(51, 41))
        self.send_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.send_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/send.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.send_btn.setIcon(icon4)
        self.send_btn.setIconSize(QtCore.QSize(50, 40))
        self.send_btn.setObjectName("send_btn")
        self.horizontalLayout_2.addWidget(self.send_btn)
        self.stackedWidget.addWidget(self.send_mess)
        self.setting_box = QtWidgets.QWidget()
        self.setting_box.setObjectName("setting_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.setting_box)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.set_lang = QtWidgets.QWidget(parent=self.setting_box)
        self.set_lang.setMaximumSize(QtCore.QSize(16777215, 141))
        self.set_lang.setObjectName("set_lang")
        self.label_2 = QtWidgets.QLabel(parent=self.set_lang)
        self.label_2.setGeometry(QtCore.QRect(9, 9, 368, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.eng_rad_btn = QtWidgets.QRadioButton(parent=self.set_lang)
        self.eng_rad_btn.setGeometry(QtCore.QRect(9, 65, 368, 22))
        self.eng_rad_btn.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.eng_rad_btn.setFont(font)
        self.eng_rad_btn.setObjectName("eng_rad_btn")
        self.vn_rad_btn = QtWidgets.QRadioButton(parent=self.set_lang)
        self.vn_rad_btn.setGeometry(QtCore.QRect(9, 93, 368, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.vn_rad_btn.setFont(font)
        self.vn_rad_btn.setObjectName("vn_rad_btn")
        self.jap_rad_btn = QtWidgets.QRadioButton(parent=self.set_lang)
        self.jap_rad_btn.setGeometry(QtCore.QRect(9, 37, 368, 22))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.jap_rad_btn.setFont(font)
        self.jap_rad_btn.setObjectName("jap_rad_btn")
        self.horizontalLayout_3.addWidget(self.set_lang)
        self.save_set_btn = QtWidgets.QPushButton(parent=self.setting_box)
        self.save_set_btn.setMaximumSize(QtCore.QSize(61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.save_set_btn.setFont(font)
        self.save_set_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save_set_btn.setStyleSheet("#save_set_btn{\n"
"    background-color: rgb(0, 255, 127);\n"
"}")
        self.save_set_btn.setObjectName("save_set_btn")
        self.horizontalLayout_3.addWidget(self.save_set_btn)
        self.stackedWidget.addWidget(self.setting_box)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # cài đặt mặc định
        self.vn_rad_btn.setChecked(True)
        wikipedia.set_lang(self.language_set())
        hour =  datetime.datetime.now().hour
        if hour >= 6 and hour< 12 :
            self.speak("Chào buổi sáng, tôi có thể giúp gì cho bạn")
        elif hour >= 12 and hour < 18 :
            self.speak("Chào buổi chiều, tôi có thể giúp gì cho bạn")
        elif hour >= 18 and hour <= 24 :
            self.speak("Chào buổi tối, tôi có thể giúp gì cho bạn")

        # chuyển stackedWidget
        self.keybord_btn.clicked.connect(self.show_mess)
        self.setting_btn.clicked.connect(self.show_setting_box)
        self.save_set_btn.clicked.connect(self.save_setting)
    
        # radion check
        self.vn_rad_btn.clicked.connect(self.vn_btn_clicked)
        self.eng_rad_btn.clicked.connect(self.eng_btn_clicked)
        self.jap_rad_btn.clicked.connect(self.jap_btn_clicked)

        # click
        self.mic_btn.clicked.connect(self.mic_click)
        self.send_btn.clicked.connect(self.send_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nerin"))
        self.label_2.setText(_translate("MainWindow", "Ngôn ngữ"))
        self.eng_rad_btn.setText(_translate("MainWindow", "English"))
        self.vn_rad_btn.setText(_translate("MainWindow", "Vietnamese"))
        self.jap_rad_btn.setText(_translate("MainWindow", "Japanese"))
        self.save_set_btn.setText(_translate("MainWindow", "Save"))

    # chuyển stackedWidget
    def show_main_box(self):
        self.stackedWidget.setCurrentIndex(0)
    def show_mess(self):
        self.stackedWidget.setCurrentIndex(1)
    def show_setting_box(self):
        self.stackedWidget.setCurrentIndex(2)
    
    # radion click
    def vn_btn_clicked(self):
        self.vn_rad_btn.setChecked(True)
        self.eng_rad_btn.setChecked(False)
        self.jap_rad_btn.setChecked(False)

    def eng_btn_clicked(self):
        self.eng_rad_btn.setChecked(True)
        self.vn_rad_btn.setChecked(False)
        self.jap_rad_btn.setChecked(False)

    def jap_btn_clicked(self):
        self.jap_rad_btn.setChecked(True)
        self.vn_rad_btn.setChecked(False)
        self.eng_rad_btn.setChecked(False)

# cài đặt ngôn ngữ
    def language_set(self):
        if self.vn_rad_btn.isChecked():
            language = 'vi'
        elif self.eng_rad_btn.isChecked():
            language = 'en'
        else:
            language = 'ja'

        return language
    
    # lưu cài đặt
    def save_setting(self):
        wikipedia.set_lang(self.language_set())
        self.show_main_box()   

    # nhập và gửi tin nhắn
    def send_message(self):
        query = self.text_query.text()
        self.chat_show.append("You: " + query)
        self.show_main_box()
        self.text_query.clear()

    
    def send_query(self):
        query = self.text_query.text()
        self.chat_show.append("You: " + query)
        self.show_main_box()
        self.text_query.clear()
        return query

    # dịch
    def trans(self, query):
        language = self.language_set()
        query =  self.translator.translate(query, src='vi', dest= language).text
        return query
    
    #chuyen van ban thanh am thanh    
    def speak(self, query):
        language = self.language_set()
        text = self.trans(query)
        self.chat_show.append("Nerin: {}".format(text))
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3", False)
        os.remove("sound.mp3")
    
    # mic
    def mic_click(self):
        self.show_main_box()
        if self.flag is None:
            self.flag = 1
            self.assistant()
        else:
            self.flag =1
            # self.check()
        
    
    def send_click(self):
        self.show_main_box()
        if self.flag is None:
            self.flag = 2
            self.assistant()
        else:
            self.flag =2
            # self.check()
        

    def check(self):
        text1 = ""
        if self.flag == 1:
            text1 = self.get_audio()
            self.flag = None 
        elif self.flag == 2:
            text1 = self.send_query()
            self.flag = None

        return text1


    #chuyen am thanh sang van ban
    def get_audio(self):
        language = self.language_set()
        c = sr.Recognizer()
        with sr.Microphone() as source: 
            c.pause_threshold = 1
            audio = c.listen(source)
        try:
            query = c.recognize_google(audio,language = language)
            self.chat_show.append(self.trans("You: " + query))
        except sr.UnknownValueError:
            self.speak("vui lòng nói lại hoặc nhập lệnh")
        
        return query
        
    #Chức năng hiển thị thời gian
    def get_time(self, query):
        now = datetime.datetime.now()
        if "giờ" in query or "time" in query or "何時" in query:
            self.speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
        elif "ngày" in query or "day" in query or "今日" in query:
            self.speak("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year)) 
        else:
            self.speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
            time.sleep(1)
            self.speak("Ngày %d tháng %d năm %d" % (now.day, now.month, now.year)) 

    # Chức năng xem dự báo thời tiết
    def current_weather(self):
        self.speak("Bạn muốn xem thời tiết ở đâu ạ.")
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        city = ""
        while True:
            if self.mic_btn.clicked.connect(self.mic_click) and self.flag == 1:
                city = self.check()
                break
            elif self.send_btn.clicked.connect(self.send_click) and self.flag == 2:
                city = self.check()
                break

            QtWidgets.QApplication.processEvents()
        if not city:
            pass
        api_key = "fe8d8c65cf345889139d8e545f57819a"
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(call_url)
        data = response.json()
        if data["cod"] != "404":
            city_res = data["main"]
            current_temperature = city_res["temp"]
            current_pressure = city_res["pressure"]
            current_humidity = city_res["humidity"]
            suntime = data["sys"]
            sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
            wthr = data["weather"]
            weather_description = wthr[0]["description"]
            now = datetime.datetime.now()
            content = """
            Hôm nay là ngày {day} tháng {month} năm {year}
            Mặt trời mọc vào {hourrise} giờ {minrise} phút
            Mặt trời lặn vào {hourset} giờ {minset} phút
            Nhiệt độ trung bình là {temp} độ C
            Áp suất không khí là {pressure} héc tơ Pascal
            Độ ẩm là {humidity}%""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                            hourset = sunset.hour, minset = sunset.minute, 
                                            temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
            self.speak(content)
            time.sleep(20)
        else:
            self.speak("Không tìm thấy địa chỉ của bạn")
            self.current_weather()

    #Chức năng tìm định nghĩa trên từ điển wikipedia
    def tell_me_about(self):
        try:
            self.speak("Bạn muốn nghe về gì ạ")
            text = ""
            while True:
                if self.mic_btn.clicked.connect(self.mic_click) and self.flag == 1:
                    text = self.check()
                    break
                elif self.send_btn.clicked.connect(self.send_click) and self.flag == 2:
                    text = self.check()
                    break

                QtWidgets.QApplication.processEvents()
            contents = wikipedia.summary(text).split('\n')
            self.speak(contents[0])
            time.sleep(20)
            for content in contents[1:]:
                self.speak("Bạn muốn nghe thêm không")
                ans = self.get_audio()
                if "có" not in ans:
                    break    
                self.self.speak(content)
                time.sleep(10)

            self.speak('Cảm ơn bạn đã lắng nghe!!!')
        except:
            self.speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
            self.tell_me_about()

    #Tìm kiếm trên gg
    def search_in_google(self):
        self.speak('Bạn muốn tìm cái gì?')
        search = ""
        while True:
            if self.mic_btn.clicked.connect(self.mic_click) and self.flag == 1:
                search = self.check()
                break
            elif self.send_btn.clicked.connect(self.send_click) and self.flag == 2:
                search = self.check()
                break

            QtWidgets.QApplication.processEvents()
    
        search = self.check()
        url = f"https://www.google.com.vn/search?q={search}"
        webbrowser.get().open(url)
        self.speak(f'Đây là kết quả tìm kiếm cho {search} trên google')

    #Mở video trên Youtube
    def Youtube(self):
        self.speak('Bạn muốn tìm cái gì?')
        search = ""
        while True:
            if self.mic_btn.clicked.connect(self.mic_click) and self.flag == 1:
                search = self.check()
                break
            elif self.send_btn.clicked.connect(self.send_click) and self.flag == 2:
                search = self.check()
                break

            QtWidgets.QApplication.processEvents()
        url = f"https://www.youtube.com/search?q={search}"
        webbrowser.get().open(url)
        self.speak(f'Đây là kết quả tìm kiếm cho {search} trên youtube')

    # goi chuc nang
    def assistant(self):
        query = self.check()
        self.flag = 0
        if "Xin chào" in query or "Chào" in query or "xin chào" in query or "chào" in query or "Hello" in query or "hello" in query or "Hi" in query or "hi" in query or "こんにちは" in query:
            self.speak("Xin chào bạn! Bạn cần tôi hỗ trợ gì không")
        elif "giờ" in query or "hiện tại" in query or "ngày" in query or "thời gian" in query or "time" in query or "day" in query or "now" in query or "今" in query or "今日" in query or"現在" in query or "何時" in query:
            self.get_time(query)
            self.flag = None
        elif "google" in query or "Google" in query:
            self.search_in_google()
        elif "youtube" in query or "YouTube" in query:
            self.Youtube()
        elif "thời tiết" in query or "weather" in query or "天気" in query:
            self.current_weather()   
        elif "định nghĩa" in query or "definition" in query or "定義" in query or "定義文" in query:
            self.tell_me_about()
        elif "facebook" in query or "Facebook" in query:
            url = f"https://www.facebook.com"
            webbrowser.get().open(url)
            self.speak('Đã mở facebook')
            self.flag = None
        elif "zalo" in query or "Zalo" in query:
            url = f"https://chat.zalo.me/?null"
            webbrowser.get().open(url)
            self.speak('Đã mở Zalo')
            self.flag = None
        elif "thoát" in query or "tạm biệt" in query or "goodbye" in query or "bye" in query:
            self.speak("Hẹn gặp lại bạn sau!")
            time.sleep(2)
            MainWindow.close()
        else:
            self.speak("Tôi không hiểu, vui lòng nói hoặc nhập lại!")
            self.flag = None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
