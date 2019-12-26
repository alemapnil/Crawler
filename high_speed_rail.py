import requests
import json as j
from bs4 import BeautifulSoup
url="http://www.thsrc.com.tw/tw/TimeTable/Search"

date=input("請輸入搭車日期，如2019/12/31  ")
start=input("請輸入起始站，如南港站  ")
end=input("請輸入終點站，如左營站  ")

if start=="南港站" :
    startcode="2f940836-cedc-41ef-8e28-c2336ac8fe68"
elif start=="台北站" :
    startcode="977abb69-413a-4ccf-a109-0272c24fd490"
elif start=="板橋站" :
    startcode="e6e26e66-7dc1-458f-b2f3-71ce65fdc95f"
elif start=="桃園站" :
    startcode="fbd828d8-b1da-4b06-a3bd-680cdca4d2cd"
elif start=="新竹站" :
    startcode="a7a04c89-900b-4798-95a3-c01c455622f4"
elif start=="苗栗站" :
    startcode="e8fc2123-2aaf-46ff-ad79-51d4002a1ef3"
elif start=="台中站":
    startcode="3301e395-46b8-47aa-aa37-139e15708779"
elif start=="彰化站" :
    startcode="38b8c40b-aef0-4d66-b257-da96ec51620e"
elif start=="雲林站":
    startcode="5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f"
elif start=="嘉義站":
    startcode="60831846-f0e4-47f6-9b5b-46323ebdcef7"
elif start=="台南站":
    startcode="9c5ac6ca-ec89-48f8-aab0-41b738cb1814"
elif start=="左營站":
    startcode="f2519629-5973-4d08-913b-479cce78a356"

if end=="南港站" :
    endcode="2f940836-cedc-41ef-8e28-c2336ac8fe68"
elif end=="台北站" :
    endcode="977abb69-413a-4ccf-a109-0272c24fd490"
elif end=="板橋站" :
    endcode="e6e26e66-7dc1-458f-b2f3-71ce65fdc95f"
elif end=="桃園站" :
    endcode="fbd828d8-b1da-4b06-a3bd-680cdca4d2cd"
elif end=="新竹站" :
    endcode="a7a04c89-900b-4798-95a3-c01c455622f4"
elif end=="苗栗站" :
    endcode="e8fc2123-2aaf-46ff-ad79-51d4002a1ef3"
elif end=="台中站":
    endcode="3301e395-46b8-47aa-aa37-139e15708779"
elif end=="彰化站" :
    endcode="38b8c40b-aef0-4d66-b257-da96ec51620e"
elif end=="雲林站":
    endcode="5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f"
elif end=="嘉義站":
    endcode="60831846-f0e4-47f6-9b5b-46323ebdcef7"
elif end=="台南站":
    endcode="9c5ac6ca-ec89-48f8-aab0-41b738cb1814"
elif end=="左營站":
    endcode="f2519629-5973-4d08-913b-479cce78a356"

d={
    "StartStationName":  start,
    "EndStationName":  end,
    "SearchType": "S",
    "StartStation": startcode,
    "EndStation": endcode,
    "DepartueSearchDate": date,
    "DepartueSearchTime": "06:00",
}

re=requests.post(url,data=d)
J=j.loads(re.text) # J is dict.
des=J["data"]["DepartureTable"]["Title"]["TitleSplit2"] #des is str.
s=[i for i in des if ord(i)<97 or ord(i)>122]
s=[i for i in s if ord(i)!=38 and ord(i)!=59]
print("將顯示從 {}至 {} 於{}的所有高鐵班次".format(start,end,"".join(s[3:-5])))

J=J["data"]["DepartureTable"]["TrainItem"] # J is list.
for i in J: # i is dict.
    print("Car no.",i["TrainNumber"])
    print("DepartureTime",i["DepartureTime"])
    print("DestinationTime",i["DestinationTime"])
    print('=======================================')
