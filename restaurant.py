import requests
from bs4 import BeautifulSoup
result=requests.get("https://www.eazydiner.com/jaipur/restaurants/near-me")
soup=BeautifulSoup(result.content,'html.parser')
divs=soup.find(id='restaurants')
c=0
for div in divs:
    c=c+1
    if c==5:
        break
    try:
        name=div.find('h3',{'itemprop':'name'}).text
        address=div.find('span',{'itemprop':'addressLocality'}).text
        title=div.find('div',{'class':'w-4-12'}).text
        cost=div.find('div',{'class':'w-8-12'}).text
        cuisine=div.find('div',{'itemprop':'servesCuisine'}).text
        offer=div.find('div',{'itemprop':'makesOffer'}).find('span').text
        print("\n>>>>>>>>>>>>>>>>>>>>>>>Welcome<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
        print("Name of restaurant:",name)
        print("Address:",address)
        print(title.strip()," : ",cost)
        print("cuisine: ",cuisine)
        print("Today's Offer: ",offer)
        
    except Exception as e:
        pass
