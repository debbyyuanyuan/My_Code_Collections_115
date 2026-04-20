import pandas as pd
import requests, json, csv, time, random
from fake_useragent import UserAgent

# pip install fake-useragent

def get_twse_data(date_str):
    
    # 使用隨機 User-Agent
    ua = UserAgent()
    
    headers = {
        'User-Agent': ua.random,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-TW,zh;q=0.9',
        'Referer': 'https://finance.yahoo.com/quote/2330.TW/',
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    # 添加時間戳防止緩存

    url = f'https://www.twse.com.tw/rwd/zh/afterTrading/BWIBBU_d?/MI_INDEX?date={date_str}&type=MS&response=json&_={int(time.time()*1000)}'
    
    # 隨機延遲
    time.sleep(random.uniform(3, 8))
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # 檢查HTTP錯誤
        
        json_data = response.json()
        
        # 檢查API狀態
        if json_data.get('stat') != 'OK':
            print(f"API回傳狀態: {json_data.get('stat')}")
            print(f"訊息: {json_data.get('msg', '無訊息')}")
            return None
            
        return json_data
        
    except Exception as e:
        print(f"錯誤: {e}")
        return None

# 執行使用
date_str = "20250108"
data = get_twse_data(date_str)

if data:
    with open('個股日本益比.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data['fields'])
        writer.writerows(data['data'])
    print("成功!")
else:
    print("取得數據失敗")