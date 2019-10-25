from bs4 import BeautifulSoup as bs
import requests
import webbrowser
v=input("Enter Query")
base = "https://www.youtube.com/results?search_query="+v
print(base)
qstring = "boddingtons+advert"
r = requests.get(base+qstring)
page = r.text
soup=bs(page,'html.parser')
vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)
for i in range(len(videolist)):
    webbrowser.open(videolist[i])
    print(videolist[i])
