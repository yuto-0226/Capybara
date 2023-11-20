import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/TTU-talk/index.html"
web = requests.get(url)                        # 取得網頁內容
soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
print(soup)
