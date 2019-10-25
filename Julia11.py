import datetime
import win32com.client
import wikipedia 
import speech_recognition as sr
import os
import smtplib
import sys
import webbrowser
from bs4 import BeautifulSoup
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob
import requests
import wolframalpha

class TwitterClient(object): 
	''' 
	Generic Twitter Class for sentiment analysis. 
	'''
	def __init__(self): 
		''' 
		Class constructor or initialization method. 
		'''
		# keys and tokens from the Twitter Dev Console 
		consumer_key = 'dZ6H7ccLUv6JvXtc0bZJzdfmr'
		consumer_secret = 'sQ8OMESFHVXWjZAJgKhun9AO08ysYpREaNCnmDmPyMMXC7ZoqQ'
		access_token = '869122786274541568-LhBEPz2HbKYEYAk6MB8SpOz0HOVk2jF'
		access_token_secret = 'k4mWyIhbAbkagpGOdR1wOe8Qs3R8WOfAqEOtG8JM5nMm6'

		# attempt authentication 
		try: 
			# create OAuthHandler object 
			self.auth = OAuthHandler(consumer_key, consumer_secret) 
			# set access token and secret 
			self.auth.set_access_token(access_token, access_token_secret) 
			# create tweepy API object to fetch tweets 
			self.api = tweepy.API(self.auth) 
		except: 
			print("Error: Authentication Failed") 

	def clean_tweet(self, tweet): 
		''' 
		Utility function to clean tweet text by removing links, special characters 
		using simple regex statements. 
		'''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 

	def get_tweet_sentiment(self, tweet): 
		''' 
		Utility function to classify sentiment of passed tweet 
		using textblob's sentiment method 
		'''
		# create TextBlob object of passed tweet text 
		analysis = TextBlob(self.clean_tweet(tweet)) 
		# set sentiment 
		if analysis.sentiment.polarity > 0: 
			return 'positive'
		elif analysis.sentiment.polarity == 0: 
			return 'neutral'
		else: 
			return 'negative'

	def get_tweets(self, query, count = 10): 
		''' 
		Main function to fetch tweets and parse them. 
		'''
		# empty list to store parsed tweets 
		tweets = [] 

		try: 
			# call twitter api to fetch tweets 
			fetched_tweets = self.api.search(q = query, count = count) 

			# parsing tweets one by one 
			for tweet in fetched_tweets: 
				# empty dictionary to store required params of a tweet 
				parsed_tweet = {} 

				# saving text of tweet 
				parsed_tweet['text'] = tweet.text 
				# saving sentiment of tweet 
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

				# appending parsed tweet to tweets list 
				if tweet.retweet_count > 0: 
					# if tweet has retweets, ensure that it is appended only once 
					if parsed_tweet not in tweets: 
						tweets.append(parsed_tweet) 
				else: 
					tweets.append(parsed_tweet) 

			# return parsed tweets 
			return tweets 

		except tweepy.TweepError as e: 
			# print error (if any) 
			print("Error : " + str(e)) 

def main(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    tweets = api.get_tweets(query = '#war', count = 200) 
  
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets
    neut=len(tweets) - len(ntweets) - len(ptweets)/len(tweets)
    if 100*len(ptweets)/len(tweets)>50:
        return 1

speaker = win32com.client.Dispatch("SAPI.SpVoice") 

def doct():
        result=requests.get("https://www.practo.com/jaipur/doctors")
        webbrowser.open("https://www.practo.com/jaipur/doctors")
        soup=BeautifulSoup(result.content,'html.parser')
        divs=soup.find('div',{'data-qa-id':'doctor_listing_cards'})
        i=0
        for div in divs:
                i=i+1
                if i==7:
                        break
                try:
                        div=div.find('div',{'class':'o-media'})
                        name=div.find('div',{'class':'c-card-info'}).find('a').text
                        speak(name)
                        print(name)
                except Exception as e:
                        pass

def email1():
        speak('Who is the recipient? ')
        recipient = takeCommand()
        if 'me' in recipient:
              try:
                      speak('What should I say? ')
                      content = takeCommand()
                      server = smtplib.SMTP('smtp.gmail.com', 587)
                      server.ehlo()
                      server.starttls()
                      server.login("aditya28071999@gmail.com", 'aditya28')
                      server.sendmail('aditya28071999@gmail.com', "pandit28071999@gmail.com", content)
                      server.close()
                      speak('Email sent!')
              except:
                      speak('Sorry Sir! I am unable to send your message at this moment!')
                       
def speak(audio):
    print(audio)
    speaker.Speak(audio)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Master !!!. Please tell me how may I help you")
def takeCommand():
   
    r = sr.Recognizer()
    start = int(datetime.datetime.now().second)
    while int(datetime.datetime.now().second)<start+1:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 15
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-in')
                print('User: ' + query + '\n')
            except sr.UnknownValueError:
                speak('Sorry sir! I didn\'t get that! Try typing the command!')
                query = str(input('Command: '))
        return query
if __name__ == "__main__":
    speak("My master name is Aditya")
    wishme()
    while True:
        if 1:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'play music' in query:
                music_dir = "D:\\song"
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'dev c++' in query:
                codePath = "C:\\Users\\admin\\Desktop\\Tor Browser\\Browser\\firefox.exe"
                os.startfile(codePath)
            elif 'cricket score' in query:
                codePath="C:\\Users\\user\\Desktop\\python\\cr1.py"
                os.startfile(codePath)
            elif 'not feeling well' in query:
                speak("Ohh!! Master you must take medicine")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening to medical query")
                    r.pause_threshold =1
                    audio = r.listen(source)
                    query = r.recognize_google(audio, language='en-in')
                    webbrowser.open(query)
            elif 'purchase' in query:
                l1=query.split(" ")
                speak("what kind of"+l1[-1])
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening to "+l1[-1]+"query")
                    r.pause_threshold =1
                    audio = r.listen(source)
                    query = r.recognize_google(audio, language='en-in')
                    webbrowser.open(query)
            elif "i want to play game" in query:
                codePath="C:\\Users\\user\\Desktop\\python\\carracing.py"
                os.startfile(codePath)
            elif "i am feeling bored" in query:
                speak(" master would you like to go for a movie or restaurant")
                l1=query.split(" ")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening to "+l1[-1]+"query")
                    r.pause_threshold =1
                    audio = r.listen(source)
                    query = r.recognize_google(audio, language='en-in')
                    if "movie" in query:
                            a=main()
                            if a==1:
                                    speak("a")
                            else:
                                    speak("d")
                        
            elif "nearest doctor" in query:
                    doct()
            elif 'news' in query:
                speak("what kind of news you want to know")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening to news query")
                    r.pause_threshold =1
                    audio = r.listen(source)
                    query = r.recognize_google(audio, language='en-in')
                    webbrowser.open(query)
            elif 'wishlist' in query:
                speak("sure sir")
                codePath= "C:\\Users\\admin\\Desktop\\Julia\\amazon_price_tracker.py"
                os.startfile(codePath)
            elif 'exit the file' in query:
                quit()
            elif "weather" in query:
                    speak("ok sir")
                    codePath="C:\\Users\\admin\\Desktop\\Julia\\weather_finder.py"
                    os.startfile(codePath)
            elif "restaurant" in query:
                    speak("you might be hungry")
                    codePath="C:\\Users\\admin\\Desktop\\Julia\\restaurant.py"
                    os.startfile(codePath)
            elif "video song" in query:
                    speak("wait sir opening")
                    codePath="C:\\Users\\admin\\Desktop\\Julia\\you_delhi.py"
                    os.startfile(codePath)
            else:
                    query=query
                    speak("Searching")
                    try:
                            try:
                                    res=win32com.client.query(query)
                                    results=next(res.results).text
                                    speak("Accoding to me -")
                                    speak("got it")
                                    speak(results)
                            except:
                                    results = wikipedia.summary(query, sentences=2)
                                    speak("got it")
                                    speak("Accoding to me -")
                                    speak(results)
                    except:
                            webbrowser.open('www.google.com'+query)
        speak('Next Command! Sir!')


