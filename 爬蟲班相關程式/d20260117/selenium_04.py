import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import requests
from bs4 import BeautifulSoup
import csv

# 直接用 undetected_chromedriver
browser = uc.Chrome()
browser.get('https://www.google.com.tw')
time.sleep(random.uniform(3, 6))

inputA = browser.find_element(By.NAME, 'q')
for char in '雲林科技大學':
    inputA.send_keys(char)
    time.sleep(random.uniform(0.07, 0.30))

inputA.send_keys(Keys.ENTER)
time.sleep(random.uniform(6, 10))

print(browser.title)

#靜態爬蟲思維
with open('d20260117_google.csv','w',newline='') as f:
    writer=csv.writer(f)
    
    sp=BeautifulSoup(browser.page_source,'html.parser')
    datatag=sp.select('.yuRUbf')
    for i in range(len(datatag)): #len(datatag)計算datatag的長度
        texts=datatag[i].find_all('h3',{'class':'LC20lb MBeuO DKV0Md'})
        for j in range(len(texts)):
            print(texts[j].text)
            writer.writerow([texts[j].text])
                  
print("抓取成功")

