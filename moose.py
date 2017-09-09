from bs4 import BeautifulSoup
import urllib.request
import re


url = 'https://mooserec.bandcamp.com/'

key = True
while key:
  try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read()
    key = False
  except:
    pass

soup = BeautifulSoup(html, "lxml")



artist = []
title = []
url = []

p = soup.prettify()

for tit in soup.find_all("p",class_="title"):
  for ex in tit.find_all('span'):
    art = re.sub('\s{2}',"",ex.text.replace('\n',''))
    artist.append(art)
    ex.extract()
  moji = re.sub('\s{2}',"",tit.text.replace('\n','')) #連続した空白の削除
  title.append(moji)

for link in soup.find_all("div",class_="leftMiddleColumns"):
  for link2 in link.find_all("a"):
    if 'https://' in link2['href']:
      url.append(link2['href'])
    else:
      url.append('https://mooserec.bandcamp.com'+link2['href'])



print(len(artist),artist)
print(len(title),title)
print(len(url),url)
