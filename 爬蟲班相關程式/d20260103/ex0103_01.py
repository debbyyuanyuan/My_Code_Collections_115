import requests, json
import pandas as pd

url='https://www.twse.com.tw/rwd/zh/afterTrading/MI_5MINS?response=json&_=1725068934083'
jsondata=requests.get(url)
#print(jsondata)
data=jsondata.json()
#print(data)
fd=data["fields"]
dd=data["data"]
df=pd.DataFrame(dd,columns=fd)
print(df)
df.to_csv('MI_5MINS.csv',encoding='utf-8',index=False)
