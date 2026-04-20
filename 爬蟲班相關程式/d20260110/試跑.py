import pandas as pd
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Accept-Language': 'zh-TW,zh;q=0.9',  # 接受的語言設定（繁體中文）
    'Accept-Encoding': 'gzip, deflate, br', # 接受的編碼方式
    'Connection': 'keep-alive', # 保持連線
    'Cache-Control': 'max-age=0', # 忽略緩存
    'Upgrade-Insecure-Requests': '1' # 支援安全升級
}

url='https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20200108&type=MS&response=json'
jsonf=requests.get(url).text
#print(jsonf)
jsontext=json.loads(jsonf)
#print(jsontext)
###取第七個資訊
table=(jsontext['tables'])[6]
#print(table)
title=table['title']
field=table['fields']
data=table['data']

###用csv套件將json轉為csv

with open('每日收盤行情.csv','w',newline='',encoding='utf-8') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(field)
    for row in data:
      writer.writerow(row)
print("已成功寫入")