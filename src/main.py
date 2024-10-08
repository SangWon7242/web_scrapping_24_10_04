import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지 요청
url = 'https://news.naver.com/section/104'  # 스크래핑할 URL
response = requests.get(url)

# 2. 요청이 성공했는지 확인

if response.status_code == 200:
  print("웹 페이지를 성공적으로 가져왔습니다!")    


# BeautifulSoup 객체 생성
# response.text는 HTML 소스 코드 텍스트임
html_data = BeautifulSoup(response.text, 'html.parser')  

# print(html_data.select('.sa_text_strong'))

headline_news_list = html_data.select('.sa_text_strong')
news_title_list = []

# 1차 가공
for news_title in headline_news_list:
  # print(news_title.get_text())
  news_title_txt = news_title.get_text()
  news_title_list.append(news_title_txt)
  
# print(news_title_list)  

# 2차 가공
for i, title in enumerate(news_title_list):
  no = i + 1
  print(f"{no} : {title}")
