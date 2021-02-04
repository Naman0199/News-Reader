# Akhbaar Padke Sunao
import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)


if __name__ == '__main__':
    speak("Top Headlines for today. lets begin...")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=31933ba067d148fdb06673b001c7a4ee"
    news = requests.get(url).text
    news_pydict = json.loads(news)
    for i in range(0,10):
        speak(news_pydict["articles"][i]["title"])
        print(news_pydict["articles"][i]["title"])
        if i>=9:
            break
        elif i==8:
            speak("So the last headline for today is")
        else:
            speak("Moving to next headline")








