import requests
from bs4 import BeautifulSoup
import time

cur_date = time.strftime("%Y-%m-%d")

vgm_url = 'http://nbt.tj/tj/kurs/export_xml.php?date=' + cur_date + '&export=xmlout'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')

a = {'840', '978', '810'}

for link in soup.find_all('valute'):
  if (link.get('id') in a):
    print( link.findChild('nominal').text, link.findChild('name').text, link.findChild('value').text, 'TJS' )
