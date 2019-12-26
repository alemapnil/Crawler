from selenium import webdriver
from bs4 import BeautifulSoup
import time
print("將印出露天拍賣的所有筆電商品及價格")
url = "https://find.ruten.com.tw/s/?q=%E7%AD%86%E9%9B%BB&style=list"
driver = webdriver.Chrome()
driver.get(url)
soup = BeautifulSoup(driver.page_source,"html.parser")
page=soup.find_all("li",{"class":["info"]}) # page[0] is tag.
allpage=int(page[0].contents[1])

for i in range(1,allpage+1):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    infos = soup.find_all("div",attrs={"class":"prod_info"}) # infos is list.
    for info in infos:
        title = info.find_all("a")
        print(title[0].text)
        price = info.find_all("span",attrs={"class": "price"}) # price is list.
        print("$"+price[0].text,end="")
        if price[1].attrs == {"class":["price"]}:
            print(" -$"+price[1].text,end="")
        print("")
        print(title[0]["href"])
    driver.find_element_by_link_text("下一頁").click()
    print("第{}頁 載完".format(i))
    time.sleep(5)
print("露天拍賣筆電商品，爬蟲結束")