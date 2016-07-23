from urllib import request
import os
import re

from bs4 import BeautifulSoup

req = request.Request("http://dota2.gamepedia.com/Emoticons", headers={'User-Agent': 'Mozilla/5.0'})

html = request.urlopen(req)
soup = BeautifulSoup(html, 'html.parser')

# get wikipedia tables
table = soup.findAll('table', {'class':'wikitable'})
# get images in first table
imgs = table[0].findAll('img')

if (not os.path.exists('emojis')):
    os.makedirs('emojis')

for img in imgs:
    src = img.get('src')
    response = request.urlopen(src)
    p = re.compile('.*([A-Z].*\.gif).*')
    result = p.match(src)
    filename = result.group(1)

    with open('emojis/' + filename, 'wb') as output:
        output.write(response.read())

    print(result.group(1))
        

