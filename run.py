from gtts import gTTS
import speech_recognition as sr
import os
from bs4 import BeautifulSoup
import webbrowser
sample_rate = 48000
chunk_size = 2048

r = sr.Recognizer()
import requests
def analyzeText(text):
    subscription_key="476082e293034834aed67e481f868c26"
    text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
    sentiment_api_url = text_analytics_base_url + "sentiment"
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}

    documents = {
        'documents': [
            {'id':'1', 'language':'en', 'text':text}
        ]
    }
    #print('Documents: ',documents)
    response  = requests.post(sentiment_api_url, headers=headers, json=documents)
    sentiments = response.json()
    if(not sentiments['errors']):
        score =  sentiments['documents'][0]['score']
    else:
        print(sentiments['errors'])
        return null
    
    if(score>0.9):
        return 'Good to be alive andy grammer'
    elif(score>0.8):
        return 'me too meghan trainor'
    elif(score>0.7):
        return 'Which witch florence and the machine'
    elif(score>0.6):
        return 'never gonna give you up rick astley'
    elif(score>0.5):
        return 'say it again frances'
    elif(score>0.4):
        return 'brand new ben rector'
    elif(score>0.3):
        return 'this girl kungs'
    elif(score>0.2):
        return 'let it all go birdy'
    elif(score>0.1):
        return '5am amber run'
    else:
        return 'take it out on me thousand foot krutch'

def getText(text):
  score = analyzeText(text)


def start(toBeSpoken):
  tts = gTTS(text=toBeSpoken, lang='en')
  tts.save("play.mp3")
  os.system("play.mp3")

def play():
  with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    print("Say Something")
    audio = r.listen(source)        
    try:
      text = r.recognize_google(audio)
      print("you said: " + text)
      return text
    except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
      return play()
    except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

def playSong(song):
  research_later = song
  goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later
  r = requests.get(goog_search)
  soup = BeautifulSoup(r.text, "html.parser")
  print(soup.find('cite').text)
  webbrowser.open(soup.find('cite').text)
  

##
##import requests
##from bs4 import BeautifulSoup
##import webbrowser
##research_later = "bran new day rayn star"
##goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later
##r = requests.get(goog_search)
##soup = BeautifulSoup(r.text, "html.parser")
##print(soup.find('cite').text)
##webbrowser.open(soup.find('cite').text)

start("how was your day")
response = play()
print('Response = ',response)
song = analyzeText(response)
start("Will you like to hear "+song)
response = play()
print('Response: ',response)
if('yes' in response):
  playSong(song)
elif('no' in response):
  pass
else:
  song = analyzeText(response)
  playSong(song)
  


