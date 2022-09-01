import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from datetime import datetime

#ignore ssl certificate error ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

header = {'User-Agent' : 'Mozilla/5.0'}

url_m = input('enter:')
url = urllib.request.Request(url_m, headers=header)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

songs = soup.find_all('div','ellipsis rank01')
singers = soup.find_all('span', 'checkEllipsis')
#현재 시간 기준 가요 탑100 출력하기
now = datetime.now()
print('현재시간: '+str(now))
i=0
for s in range(len(songs)):
    print(f'{i+1}위')
    print(f'{songs[i].text.strip()}',end=" - ")
    print(singers[i].text.strip())
    i += 1
    print()