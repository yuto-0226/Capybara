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

def get_web(url):
    return requests.get(url)

# 回傳文章物件
def get_posts(url: str) -> dict:
    data = [{}]
    web = get_web(url)
    soup = BeautifulSoup(web.text, "html.parser")
    
    for item in soup.find_all("div",class_="r-ent"):
        title = item.find('div', class_='title').getText().strip()
        link = root + item.find('div', class_='title').a['href'].strip()
        author = item.find('div', class_='author').getText().strip()
        obj = {
            "title": title,
            "link": link,
            "author": author
        }
        data.insert(0,obj)
    return data

def main():
    url = query("TTU-talk",["資工"],1)
    articles = get_posts(url)
    print(articles)

# 若執行進入點為此檔案則執行以下
if __name__ == "__main__":
    import requests
    import requests_html
    from bs4 import BeautifulSoup
    main()