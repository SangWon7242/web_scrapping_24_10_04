import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지 요청
url = 'https://slogads.com'  # 스크래핑할 URL
response = requests.get(url)
# print(response.status_code)

# 2. 요청이 성공했는지 확인
if response.status_code == 200:
    print("웹 페이지를 성공적으로 가져왔습니다!")       
