import pyttsx3
import speech_recognition as sr
import math

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def add1(query):
    l=query.split('and')
    c=[]
    for k in l:
        n=''
        for i in k:
            try:
                if int(i) in range(10):
                    n=n+i
            except:
                pass
        c.append(n)
    q=int(c[0])+int(c[1])    
    return q
def subt(query):
    t="from" if "from" in query else "-"
    l=query.split(t)
    c=[]
    for k in l:
        n=''
        for i in k:
            try:
                if int(i) in range(10):
                    n=n+i
            except:
                pass
        c.append(n)
    q=int(c[1])-int(c[0])    
    return q

def div(r):
    t="by" if "by" in r else "divide"
    l=query.split(t)
    c=[]
    for k in l:
        n=''
        for i in k:
            try:
                if int(i) in range(10):
                    n=n+i
            except:
                pass
        c.append(n)
    q=int(c[0])/int(c[1])    
    return q

def square1(x):
    l=query.split("square of")
    c=[]
    for k in l:
        n=''
        for i in k:
            try:
                if int(i) in range(10):
                    n=n+i
            except:
                pass
        c.append(n)
    q=int(c[1])*int(c[1])    
    return q

    return x*x

def sin1(x):
    t="sine of" if "sine" in x else "sin of"
    l=query.split(t)
    c=[]
    for k in l:
        n=''
        for i in k:
            try:
                if int(i) in range(10):
                    n=n+i
            except:
                pass
        c.append(n)
    q=math.sin(int(c[1]))    
    return q
def tan1(x):
    t="tan of" if "sine" in x else "tangent of"
    l=query.split(t)
    c=[]
    for k in l:
        n=''
        for i in k:
            try:
                if int(i) in range(10):
                    n=n+i
            except:
                pass
        c.append(n)
    q=math.tan(int(c[1]))    
    return q
def cos1(x):
    t="cos of" if "cos of" in x else "cosine of"
    l=query.split(t)
    c=[]
    for k in l:
        n=''
        for i in k:
            try:
                if int(i) in range(10):
                    n=n+i
            except:
                pass
        c.append(n)
    q=math.cos(int(c[1]))    
    return q

def cosec1(x):
    l=query.split("cosec of")
    c=[]
    for k in l:
        n=''
        for i in k:
            try:
                if int(i) in range(10):
                    n=n+i
            except:
                pass
        c.append(n)
    q=math.cosec(int(c[1]))    
    return q
def cot1(x):
    l=query.split("cot")
    c=[]
    for k in l:
        n=''
        for i in k:
            try:
                if int(i) in range(10):
                    n=n+i
            except:
                pass
        c.append(n)
    q=math.cot(int(c[1]))    
    return q
def log1(x):
    l=query.split("log")
    c=[]
    for k in l:
        n=''
        for i in k:
            try:
                if int(i) in range(10):
                    n=n+i
            except:
                pass
        c.append(n)
    q=math.log(int(c[1]))    
    return q


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =3
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Master said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    speak("My master name is Aditya")
    while True:
        if 1:
            query = takeCommand().lower()
            if "into" or "multiply" in query:
                y=mul(query)
                speak(y)
            elif "add" or "sum of" in query:
                a=add1(query)
                speak(a)
            elif "from" in query:
                v=subt(query)
                speak(v)
            elif "by" or "divide" in query:
                g=div(query)
                k=speak(g)
            elif "square of" in query:
                q=square1(query)
                speak(q)
                
            
