import requests
from bs4 import BeautifulSoup

r = requests.get("https://in.bookmyshow.com/jaipur")

soup = BeautifulSoup(r.content, 'html5lib')
percs = []

title = soup.findAll('h4', attrs = {'class': 'title'})
perc_text = soup.findAll('div', attrs = {'class': '__percentage'})

print(title)
for i in range(len(perc_text)):
    perc = {}
    perc['movie'] = title[i].text
    perc['likes'] = perc_text[i].text
    if(perc['likes'].find('k') == -1):
        perc['likes'] = perc['likes'].strip('%')
        percs.append(perc)

for i in range(len(percs)):
    per=percs[i]
    if per['movie']=='War':
        print(per['likes'])
