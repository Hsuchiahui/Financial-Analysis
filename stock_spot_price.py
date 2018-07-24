import requests
import time
import json
from threading import Timer
import matplotlib.pyplot as plt
import pandas as pd
class Crawler:
    
    def get_stock_price(self, url):
        self.url = url + str(int(time.time()*1000))
        response = requests.get(self.url)
        with open('financial_analysis.json', 'w', encoding='utf-8-sig') as f:
            f.write(response.text+'\n')
        #讀取寫好的'financial_analysis.json'中['msgArray'][0]['z']欄位(即期股票資訊)
        with open('financial_analysis.json', 'r', encoding='utf-8-sig') as f:
            stock_price = json.load(f)
            price = stock_price['msgArray'][0]['z']
            sysTime = stock_price['queryTime']['sysTime']
        return price, sysTime

price = Crawler()
url_1 = "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_2104.tw&json=1&delay=0&_="  
url_2 = "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_2105.tw&json=1&delay=0&_=" 
url_3 = "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_2106.tw&json=1&delay=0&_="
         
data_1 = []
data_2 = []
data_3 = []
dataTime = []
def showPrice():
    data = [] 
    data_1.append(price.get_stock_price(url_1)[0])
    data.append(price.get_stock_price(url_1))
    dataTime.append(price.get_stock_price(url_1)[1])
    #print(price.url)
    data_2.append(price.get_stock_price(url_2)[0])
    data.append(price.get_stock_price(url_2))
    #print(price.url)
    data_3.append(price.get_stock_price(url_3)[0])
    data.append(price.get_stock_price(url_3))
    #print(price.url)
    #print(data)  #列出每次三家公司的data
    global t
    t = Timer(5, showPrice)
    t.start()

t = Timer(5, showPrice)
t.start()

time.sleep(36)
t.cancel()
#print(data_1,data_2,data_3)
data_1_new = [float(i) for i in data_1]
data_2_new = [float(i) for i in data_2]
data_3_new = [float(i) for i in data_3]

dict = {"CSRC(2104)":data_1_new,"Cheng-Shin Rubber Inc(2105)":data_2_new,"kenda Tire(2106)":data_3_new}
df = pd.DataFrame(dict)
print(df)

plt.figure(figsize=(16, 9))
plt.plot(dataTime,data_1_new,dataTime,data_2_new,dataTime,data_3_new)
plt.ylim((30, 48))
plt.title('Taiwan Rubber industry(Spot Stock Price)')
plt.legend(["CSRC", "Cheng-Shin Rubber Inc","kenda Tire"], loc=1)
plt.show()

