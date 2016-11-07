    #importing necessary modules.
import bs4 as bs
import urllib.request
from gtts import gTTS
import  vlc
import time
from mutagen.mp3 import MP3

    #defining function to play sound.
def reader(s):
    tts = gTTS(text=s, lang='en')
    tts.save("greeting.mp3")
    p = vlc.MediaPlayer("greeting.mp3")
    f = MP3("greeting.mp3")
    n = f.info.length
    p.play()
    time.sleep(n)

    #connecting to news site
sauce = urllib.request.urlopen('https://news.google.co.in/').read()
soup = bs.BeautifulSoup(sauce,'lxml')
b=soup.body
y=''
m=''

m="hello boss, you should check out following news \n"
reader(m)

    #Webscraping text news with class esc-lead-title-wrapper
for x in b.find_all("div", class_="esc-lead-article-title-wrapper"):
    y="\n"+x.text+"\n"
    reader(y)

m=" \nThank you. that's all for the news today \n "
reader(m)














