import requests
import time
import json
from threading import Timer
import matplotlib.pyplot as plt
import pandas as pd
import pprint
URL_upper = "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_"
URL_lower = ".tw&json=1&delay=0&_="  
i = input("Please enter the Stock Code:(台橡TSRC:2103)")
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

data_1 = []
data_2 = []
data_3 = []
data_i = []
dataTime = []
def showPrice():
    dataTime.append(price.get_stock_price(URL_upper + str(2104) + URL_lower)[1])
    data_1.append(price.get_stock_price(URL_upper + str(2104) + URL_lower)[0])
    data_2.append(price.get_stock_price(URL_upper + str(2105) + URL_lower)[0])
    data_3.append(price.get_stock_price(URL_upper + str(2106) + URL_lower)[0])
    data_i.append(price.get_stock_price(URL_upper + i + URL_lower)[0])



t = Timer(5, showPrice)
t.start()

for _ in range (5):
    showPrice()
    time.sleep(5)

t.cancel()

data_1_new = [float(i) for i in data_1]
data_2_new = [float(i) for i in data_2]
data_3_new = [float(i) for i in data_3]
data_i_new = [float(i) for i in data_i]
dict = {"CSRC(2104)":data_1_new,"Cheng-Shin Rubber Inc(2105)":data_2_new,"kenda Tire(2106)":data_3_new,"your stock":data_i_new}
#df = pd.DataFrame(dict)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dict)

plt.figure(figsize=(16, 9))
plt.plot(dataTime,data_1_new,dataTime,data_2_new,dataTime,data_3_new,dataTime,data_i_new)
#plt.ylim((10, 48))
plt.title('Taiwan Rubber Top3 industry(Spot Stock Price)')
plt.legend(["CSRC", "Cheng-Shin Rubber Inc","kenda Tire","your stock"], loc=1)
plt.show()

