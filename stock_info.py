import matplotlib.pyplot as plt
import pandas as pd

url = 'http://www.twse.com.tw/en/exchangeReport/BWIBBU_d?response=csv&date=20180723&selectType=11'

Rubber_Inc_stock = pd.read_csv(url,skiprows=[0],encoding = 'big5')
#print(Rubber_Inc_stock)
Rubber_Inc_stock = Rubber_Inc_stock [:12]
x = Rubber_Inc_stock['Security Code']
print(x)

y = Rubber_Inc_stock['Dividend yield (%)']
y1 = Rubber_Inc_stock['P/E ratio']
y2 = Rubber_Inc_stock['P/B ratio']

dict = {'Security Code':x,'Dividend yield':y,'P/E ratio':y1,'P/B ratio':y2}
df = pd.DataFrame(dict)
df = df.set_index('Security Code')
new_df = df.replace(to_replace='-', value=0)  #將闕漏的資料補0
print(new_df)
new_df = df.replace(to_replace='-', value=0, inplace=True)
y1_convert = df['P/E ratio']

y_new = [float(i) for i in y]
y1_new = [float(i) for i in y1_convert]
y2_new = [float(i) for i in y2]


plt.figure(figsize=(16, 9))
plt.plot(x,y_new)
plt.xlabel('Security Code')
plt.title('Taiwan Rubber industry')
plt.legend(['Dividend yield(%)'], loc=1)

plt.figure(figsize=(16, 9))
plt.plot(x,y1_new,color='red')
plt.xlabel('Security Code')
plt.title('Taiwan Rubber industry')
plt.legend(['P/E ratio'], loc=1)

plt.figure(figsize=(16, 9))
plt.plot(x,y2_new,color='green')
plt.xlabel('Security Code')
plt.title('Taiwan Rubber industry')
plt.legend(['P/B ratio'], loc=1)
plt.show()