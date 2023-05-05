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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch

#khai bao bien mac dinh
wikipedia.set_lang('vi')
language = 'vi'
# path = ChromeDriverManager().install()nerin

#chuyen van ban thanh am thanh
def speak(text):
    print("Nerin: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")

#chuyen am thanh sang van ban
def get_audio():
    c = sr.Recognizer()
    with sr.Microphone() as source: 
        c.pause_threshold = 1
        audio = c.listen(source)
    try:
        text = c.recognize_google(audio,language ="vi-VN")
        print("Nerin: " + text)
    except sr.UnknownValueError:
        print("vui lòng lặp lại hoặc gõ lệnh.")
        text = str(input('Yêu cầu của bạn là: '))
    return text

def stop():
    speak("Hẹn gặp lại bạn sau!")

#nhan dang am thanh nguoi noi
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i<2:
            speak("Xin lỗi tôi nghe không rõ, bạn nói lại được không?")
    time.sleep(2)
    stop()
    return 0

#chào hỏi
# def welcome():
#     hour =  datetime.datetime.now().hour
#     if hour >= 6 and hour< 12 :
#         speak("Chào buổi sáng")
#     elif hour >= 12 and hour < 18 :
#         speak("Chào buổi chiều")
#     elif hour >= 18 and hour <= 24 :
#         speak("Chào buổi tối")
#     speak('Tôi có thể giúp gì cho bạn?')

def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))

#hiển thị thời gian
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year))
    else:
        speak("Xin lỗi, bạn có thể nói lại được không?")

#Mở ứng dụng hệ thống
def open_app(text):
    if "google" in text:
        speak("Đang mở google chrome")
        os.startfile('C:\Program Filestuan\Google\Chrome\Application\chrome.exe')
    elif "word" in text:
        speak("Đang mở Microsoft Word")
        os.startfile('\\Microsoft Office\Office16.WINWORD.EXE')
    elif "excel" in text:
        speak("Đang mở Microsoft Excel")
        os.startfile('\\Microsoft Office\Office16.EXCEL.EXE')
    elif "powerpoint" in text:
        speak("Đang mở Microsoft Powerpoint")
        os.startfile('\\Microsoft Office\Office16.POWERPNT.EXE')
    else:
        speak("Ứng dụng chưa được cài đặt")

#Mở trang web cụ thể
# def open_web(text):
#     reg_ex = re.search('Mở (.+)'. text)
#     if reg_ex:
#         domain = reg_ex.group(1)
#         url = 'https://www.' + domain
#         webbrowser.open(url)
#         speak("Đã mở trang web bạn yêu cầu")
#         return True
#     else:
#         return False

#Tìm kiếm trên gg
def search_in_google(text):
    speak('Bạn muốn tìm cái gì?')
    search = get_text().lower()
    url = f"https://www.google.com.vn/search?q={search}"
    webbrowser.get().open(url)
    speak(f'Đây là kết quả tìm kiếm cho {search} trên google')

#Gửi email
def send_email(text):
    speak("Bạn muốn gửi mail cho ai vậy?")
    recipient = get_text()
    if recipient:
        speak("Nội dung bạn muốn gửi là gì ạ?")
        content = get_text()
        mail = smtplib.SMTP('smtp.gamil.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('tuan.lt.61cntt@ntu.edu.vn','nerin060301')
        mail.sendmail('lethanhtuangam@gmail.com', content.encode('utf-8'))
        mail.close()
        speak("Mail đã được gửi")
    else:
        speak("Không tìm thấy người này")

#Xem dự báo thời tiết
def weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
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
        speak(content)
        time.sleep(20)
    else:
        speak("Không tìm thấy địa chỉ của bạn")
        weather()

#Mở video trên Youtube
def Youtube():
    speak('Bạn muốn tìm cái gì?')
    search = get_text().lower()
    url = f"https://www.youtube.com/search?q={search}"
    webbrowser.get().open(url)
    speak(f'Đây là kết quả tìm kiếm cho {search} trên youtube')

#Tìm kiếm thông tin trên wikipedia
def tell_me_about(text):
    try:
        speak("Bạn muốn nghe về gì ạ")
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = get_text()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(10)

        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
        tell_me_about()

#main
# if __name__ == "__main__":
#     # welcome()
#     while True:
#         text = get_text()
#         if "thoát" in text or "tạm biệt" in text or "dừng" in text or "ngủ thôi" in text:
#              stop()
#              break
#         elif "giờ" in text or "ngày" in text:
#             get_time(text)
#         elif "mở" in text:
#             if 'mở google và tìm kiếm' in text:
#                 search_in_google(text)
#             elif "." in text:
#                 open_web(text)
#             else:
#                 open_app(text)
#         elif "email" in text or "mail" in text or "gmail" in text:
#             send_email(text)
#         elif "định nghĩa" in text:
#             tell_me_about()
#         elif "thời tiết" in text:
#             weather()

def assistant():
    speak("Xin chào, bạn tên là gì nhỉ?")
    name = get_text()
    if name:
        speak("Chào bạn {}".format(name))
        speak("Bạn cần Bot Alex có thể giúp gì ạ?")
        while True:
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "ngủ thôi" in text:
                stop()
                break
            # elif "có thể làm gì" in text:
            #     help_me()
            elif "chào trợ lý ảo" in text:
                hello(name)
            elif "hiện tại" in text:
                get_time(text)
            elif "mở" in text:
                if 'mở google và tìm kiếm' in text:
                    search_in_google(text)
                # elif "." in text:
                #     open_web(text)
                else:
                    open_app(text)
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
            elif "thời tiết" in text:
                weather()
            elif "youtube" in text:
                Youtube()
            # elif "hình nền" in text:
            #     change_wallpaper()
            # elif "đọc báo" in text:
            #     read_news()
            elif "định nghĩa" in text:
                tell_me_about()
            else:
                speak("Bạn cần Bot giúp gì ạ?")

assistant()
