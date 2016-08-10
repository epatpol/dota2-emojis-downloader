import urllib3
import yaml
import os
import re

from bs4 import BeautifulSoup

http = urllib3.PoolManager()
r = http.request('get', 'http://dota2.gamepedia.com/Emoticons')

soup = BeautifulSoup(r.data, 'html.parser')

# get wikipedia tables
table = soup.findAll('table', {'class':'wikitable'})
# get images in first table
imgs = table[0].findAll('img')

if (not os.path.exists('emojis')):
    os.makedirs('emojis')

for img in imgs:
    src = img.get('src')
    p = re.compile('.*([A-Z].*\.gif).*')
    result = p.match(src)
    filename = result.group(1)
    if not os.path.isfile('emojis/' + filename):

        response = request.urlopen(src)

        with open('emojis/' + filename, 'wb') as output:
            output.write(response.read())

