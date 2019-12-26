
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time
no=int(input("請輸入股票代號: "))
y=int(input("請輸入年分，如2019(不可輸入未來年分) "))
m=int(input("請輸入月份，如01(不可輸入未來月份) "))
print("將輸出{}於{}年1月至{}月的個股日本益比、殖利率、股價淨值比".format(no,y,m))
print("")


def parser(y,m,d,no):
    y=str(y)
    m=str(m).zfill(2)
    d=str(d)
    no=str(no)
    url='https://www.twse.com.tw/exchangeReport/BWIBBU?response=json&date={}{}{}&stockNo={}&_=1574423593367'.format(y,m,d,no)

    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    re=requests.get(url,headers=headers)
    dic=json.loads(re.text)
    data=str(dic["data"])
    data=data.replace("\'","\"")
    df=pd.read_json(data,orient="values")
    csv=df.to_csv(header=False,index=False,encoding="utf-8-sig", line_terminator='\n')

    with open("{}.csv".format(no),"a") as f:
        f.write(csv)
    return "{}月的{}.csv已載入".format(m,no)
for i in range(1,m+1):
    print(parser(y,i,1,no))
    time.sleep(3)


