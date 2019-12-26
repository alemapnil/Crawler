import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
print("即將下載圖片")
re=requests.get("https://disp.cc/b/62-6MJ7",headers=headers)
re=re.text
soup=BeautifulSoup(re,"html.parser")
a=soup.find_all("a")
for i in a: # i is tag.
    if "http://i.imgur.com/" in i['href']: # i['href']  str.
        n=i['href'] # n is str.
        n=n.split("/")[-1]
        pic=requests.get(i['href'],headers=headers) # pic response.
        with open(n,"wb") as f:
            f.write(pic.content)
            print(n,"下載完成")



