import matplotlib.pyplot as plt
import pandas as pd

url = 'http://www.twse.com.tw/en/exchangeReport/BWIBBU_d?response=csv&date=20180723&selectType=11'

Rubber_Inc_stock = pd.read_csv(url,skiprows=[0],encoding = 'big5')
Rubber_Inc_stock = Rubber_Inc_stock [:12]
x = Rubber_Inc_stock['Security Code']

y = Rubber_Inc_stock['Dividend yield (%)']
y1 = Rubber_Inc_stock['P/E ratio']
y2 = Rubber_Inc_stock['P/B ratio']

dict = {'Security Code':x,'Dividend yield':y,'P/E ratio':y1,'P/B ratio':y2}
#df = pd.DataFrame(dict,index = x)
df = pd.DataFrame(dict)

print(df)

plt.figure(figsize=(16, 9))
plt.xlabel('Security Code')
plt.plot(x,y)
plt.title('Taiwan Rubber industry')
plt.legend(['Dividend yield(%)'], loc=1)

plt.figure(figsize=(16, 9))
plt.plot(x,y1,color='red')
plt.title('Taiwan Rubber industry')
plt.legend(['P/E ratio'], loc=1)

plt.figure(figsize=(16, 9))
plt.plot(x,y2,color='green')
plt.title('Taiwan Rubber industry')
plt.legend(['P/B ratio'], loc=1)
plt.show()