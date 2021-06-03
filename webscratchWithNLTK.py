import pyaudio
from gtts import gTTS
import os
import speech_recognition as sr
import webbrowser as wb
import random
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from translate import Translator
r =  sr.Recognizer()

with sr.Microphone() as source :
    r.adjust_for_ambient_noise(source, duration = 5)
    print('say Something')
    audio = r.listen(source)
try : 
    text = r.recognize_google(audio)
    print(text)

except Exception as e:
    print(e)  
tokenisedlist = text.split()
if "news" in tokenisedlist:
    r = requests.get("http://www.timesnownews.com/india")
    soup = BeautifulSoup(r.content,"lxml")
    g_data = soup.find_all("div",{"class":"info"})
    
    str = ''
    
    for item in g_data:
        
        str = str + ''.join(item.text)
       
    g1_data = soup.find_all("div",{"class":"catnewsBox2"})
    
    for item1 in g1_data:
       
        str = str + ''.join(item1.text)

    print(str)
    myobj = gTTS(text=str, lang='en')
    myobj.save("welcome.mp3")
    os.startfile("welcome.mp3")

if "weather" in tokenisedlist:
    r1 = requests.get("https://www.weather-forecast.com/locations/Patiala/forecasts/latest")
    soup1 = BeautifulSoup(r1.content,"lxml")
    g_data = soup1.find_all("span",{"class":"temp"})
    l1 = []
    for item2 in g_data:
        l1.append(item2.text)
    str1 = l1[-4]
    str1new = str1[0:2]
    str1final = "the temperature today is "+str1new+" degree celsius."
    print(str1)
    l2 = []
    g1_data = soup1.find_all("div",{"class":"mid"})
    for item3 in g1_data:
     l2.append(item3.text)
    str2 = l2[0]
    print(str2)
    str3 = str2[4:]
    print(str3)
    str4 = str1final+" The weather would be "+str3+" today"
    myobj = gTTS(text=str4, lang='en')
    myobj.save("welcome1.mp3")
    os.startfile("welcome1.mp3")
    
if "translate" in tokenisedlist:
    r2 =  sr.Recognizer()

    with sr.Microphone() as source1 :
        r2.adjust_for_ambient_noise(source, duration = 5)
        print('say sentence to translate')
        audio1 = r2.listen(source1)
    
    try : 
        text11 = r2.recognize_google(audio1)
        print('you said ' + text11)

    except Exception as e:
        print(e)    

    translator= Translator(to_lang="ja")
    translation = translator.translate(text11)
    print(translation)

    myobj = gTTS(text=translation, lang='ja')
    myobj.save("welcome3.mp3")
    os.startfile("welcome3.mp3")
    
if "music" in tokenisedlist:
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    r =  sr.Recognizer()
    with sr.Microphone() as source :
        r.adjust_for_ambient_noise(source, duration = 8)
        print('What is your mood today')
        audio = r.listen(source)
    try : 
        text3 = r.recognize_google(audio)
        print(text3)
    except Exception as e:
        print(e)
    yourmood = text3.split()
    score = 0
    if "very"and"sad" in yourmood:
        score = 0
    elif "sad" in yourmood:
        score = 1
    elif "low" in yourmood:
        score = 1
    elif "not"and"good" in yourmood:
        score = 2
    elif "tired" in yourmood:
        score = 3
    elif "tiring" in yourmood:
        score = 3
    elif "troublesome" in yourmood:
        score = 3
    elif "hard"and"day" in yourmood:
        score = 3
    elif "sleepy" in yourmood:
        score = 3
    elif "good" in yourmood:
        score = 4
    elif "lovely" in yourmood:
        score = 4
    elif "cool" in yourmood:
        score = 4
    elif "very"and"happy" in yourmood:
        score = 5
    elif "happy" in yourmood:
        score = 4
    elif "awesome" in yourmood:
        score = 5
    elif "gym" in yourmood:
        score = 6
    elif "running" in yourmood:
        score = 6
    elif "working"and"out" in yourmood:
        score = 6
    elif "romance" in yourmood:
        score = 7
    elif "romantic" in yourmood:
        score = 7
    elif "love" in yourmood:
        score = 7
    elif "dance" in yourmood:
        score = 8
    elif "dancing" in yourmood:
        score = 8

    print(score)
    if score==0:
        mymusicstr = "ambient"
    if score==1 or score==2:
        mymusicstr = "country"
    if score==3:
        mymusicstr = "rbsoul"
    if score==4:
        mymusicstr = "indie"
    if score==5:
        mymusicstr = "hiphoprap"
    if score==6:
        mymusicstr = "drumbass"
    if score==7:
        mymusicstr = "piano"
    if score==8:
        mymusicstr = "danceedm"
    print("your genre "+mymusicstr)

    r1 = requests.get("https://soundcloud.com/charts/top?genre="+mymusicstr)
    soup1 = BeautifulSoup(r1.content,"lxml")
    musiclist = []
    for link in soup1.find_all("a"):
        musiclist.append(link.get("href"))
        
    musicnumber = random.randint(47,101)
    print(len(musiclist))
    musicme = musiclist[musicnumber]
    musicme = musicme[1:]
    k = musicme.find("/")
    musicme = musicme[k+1:]
    finallink = "https://www.youtube.com/results?search_query="+musicme

    print(musicme)
    r2 = requests.get(finallink)
    page = r2.text
    soup2=BeautifulSoup(page,'html.parser')
    vids = soup2.findAll('a',attrs={'class':'yt-uix-tile-link'})
    videolist=[]
    for v in vids:
        tmp = 'https://www.youtube.com' + v['href']
        videolist.append(tmp)
    final = videolist[0]
    wb.get(chrome_path).open(final)
