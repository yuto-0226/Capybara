from crawler import *

class PTTcrawler():
    def __init__():
        root = "https://www.ppt.cc"

def main():
    url = "https://www.ptt.cc/bbs/TTU-talk/index.html"
    web = requests.get(url)                        # 取得網頁內容
    soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
    print(soup)

# 若執行進入點為此檔案則執行以下
if __name__ == "__main__":
    main()