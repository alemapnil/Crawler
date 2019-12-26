import requests
from bs4 import BeautifulSoup
url="https://www.ptt.cc/ask/over18"
d={
   'from': '/bbs/HatePolitics/index.html',
    'yes': 'yes'
}
print("批踢踢實業坊  看板HatePolitics :")
print("")
re=requests.post(url,data=d)
soup=BeautifulSoup(re.text,"html.parser")
divs=soup.find_all("div",class_="r-ent")
for div in divs:
    if div.a==None:
        print("本文已被刪除")
        print("============")
        continue
    print(div.a.text)
    aut=div.find_all("div",class_="author")
    print(aut[0].text)
    dat=div.find_all("div",class_="date")
    print(dat[0].text)
    print("=================")