from crawler import *

root = "https://www.ptt.cc"

# 回傳一個 url 字串
# args: 版面, 關鍵字(list), 頁數
def query(board: str, keywords: list, page: int) -> str:
    url = root
    url += f"/bbs/{board}/"
    
    if keywords is not None:
        url+="search?q="
        for words in keywords:
            url+=words
            if words != keywords[-1]:
                url+="+"
    
    if page is not None:
        if keywords is not None:
            url+=f"&page={page}"
        else:
            url+=f"page={page}"
    
    return url

def main():
    url = query("TTU-talk",["資工"],1)
    print(url)
    web = requests.get(url)                        # 取得網頁內容
    soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
    print(soup)

# 若執行進入點為此檔案則執行以下
if __name__ == "__main__":
    import requests
    import requests_html
    from bs4 import BeautifulSoup
    main()