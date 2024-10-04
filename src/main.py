import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지 요청
url = 'https://naver.com'  # 스크래핑할 URL
response = requests.get(url)

# 2. 요청이 성공했는지 확인
'''
if response.status_code == 200:
  print("웹 페이지를 성공적으로 가져왔습니다!")    
'''  
  
html = """
<nav class="menu-box-1" id="menu-box">
  <ul>
    <li>
      <a class="naver" href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a class="google" href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a class="daum" href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
"""     

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

print(soup)

# find, fint_all 연습
print(soup.find('li')) # 엘리먼트가 li인 녀석 중에서 첫 번째 li를 찾아서 반환
print(soup.find_all('li'))

find_li = soup.find_all('li')

for i, li in enumerate(find_li):
  print(f"{i} : {li}")
  
print(soup.find_all('a'))  

for i, a in enumerate(soup.find_all('a')):
  a_txt = a.get_text()
  print(f"{i} : {a_txt}")