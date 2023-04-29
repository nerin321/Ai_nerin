import speech_recognition as sr 
from gtts import gTTS 
import os 
import time 
import playsound 
import datetime
import webbrowser as wb
import wikipedia
import requests

#biến mặc định 
wikipedia.set_lang('vi')

#chuyển văn bản thành âm thanh 
def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang='vi')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("voice.mp3")

#chuyển âm thanh thành văn bản 
def command() :
    c = sr.Recognizer()
    with sr.Microphone() as source: 
        c.pause_threshold = 1
        audio = c.listen(source)
    try:
        text = c.recognize_google(audio,language ='vi')
        print("Nerin: " + text)
    except sr.UnknownValueError:
        print("vui lòng lặp lại hoặc gõ lệnh.")
        text = str(input('Yêu cầu của bạn là: '))
    return text

#thoát
def stop():
    speak("Hẹn gặp lại bạn sau!")

#chào hỏi
def welcome():
    hour =  datetime.datetime.now().hour
    if hour >= 6 and hour< 12 :
        speak("Chào buổi sáng")
    elif hour >= 12 and hour < 18 :
        speak("Chào buổi chiều")
    elif hour >= 18 and hour <= 24 :
        speak("Chào buổi tối")
    time.sleep(2)
    speak('Tôi có thể giúp gì cho bạn?')

#Chức năng hiển thị thời gian
def get_time(query):
    now = datetime.datetime.now()
    if "giờ" in query:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in query:
        speak("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year))

# Chức năng xem dự báo thời tiết
def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = command()
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
        current_weather()


#Chức năng tìm định nghĩa trên từ điển wikipedia
def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        text = command()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = command()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(10)

        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
        tell_me_about()

if __name__ == "__main__" :
    welcome()
    while True:
        query = command().lower()
        if "google" in query :
            speak('Bạn muốn tìm cái gì?')
            search = command().lower()
            url = f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            speak(f'Đây là kết quả tìm kiếm cho {search} trên google')
        elif "youtube" in query :
            speak('Bạn muốn tìm cái gì?')
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Đây là kết quả tìm kiếm cho {search} trên youtube')
        elif "facebook" in query :
            url = f"https://www.facebook.com"
            wb.get().open(url)
            speak('Đã mở facebook')
        elif "zalo" in query :
            url = f"https://chat.zalo.me/?null"
            wb.get().open(url)
            speak('Đã mở zalo')
        elif "giờ" in query or "ngày" in query:
            get_time(query)
        elif "định nghĩa" in query:
            tell_me_about()
        elif "thời tiết" in query:
            current_weather()
        elif "thoát" in query or "tạm biệt" in query or "dừng" in query or "ngủ thôi" in query:
             stop()
             break
        