import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
music = soup.select('#body-content > div.newest-list > div.music-list-wrap > table.list-wrap > tbody > tr')

# 반복문을 돌리기
count = 1
for m in music:
    # movie 안에 a 가 있으면,
    # rank = m.select_one('td.number').text
    artist = m.select_one('td.info > a.artist').text.strip()
    title = m.select_one('td.info > a.title').text.strip()

    if artist is not None:
        print(str(count) + ' / ' + title + ' / ' + artist)
        count += 1

