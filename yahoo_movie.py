import requests
import bs4
from bs4 import BeautifulSoup,element
from urllib.request import urlopen
print("Yahoo最新電影&導演演員一覽表 :")
print("")
requests=requests.get("https://movies.yahoo.com.tw")
soup=BeautifulSoup(requests.text,"html.parser")
news=soup.find_all("div",class_="ovr_btn_info")
for new in news:
    a=new.find_all("a")
    for i in a:
        u=urlopen(i["href"])
        text=u.read().decode("utf-8")
        soup=BeautifulSoup(text,"html.parser")
        m=soup.find_all("div",class_="movie_intro_list") #m list 裡面有兩個  m[0]導演 m[1]演員  m[0] is tag
        title=soup.title.string
        title=title.split("-")[0]
        print(title)
        print("導演: ",end="")
        for D in m[0].contents: #m[0].contents is list
            if type(D)==bs4.element.Tag:
                print(D.string,end="")
            else:
                try:
                    ord(D)==10
                except:
                    for i in D:
                        if ord(i)==10 or ord(i)==32:
                            continue
                        print(i,end="")                               
                else:
                    continue
        print("")
        print("演員: ",end="")
        for A in m[1].contents:
            
            if type(A)==bs4.element.Tag:
                print(A.string,end="")
            else:
                try:
                    ord(A)==10
                except:
                    for i in A:
                        if ord(i)==10 or ord(i)==32:
                            continue
                        print(i,end="")                               
                else:
                    continue
        print("")
        print("========================================================")