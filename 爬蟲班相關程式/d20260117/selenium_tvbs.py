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
browser.get('https://news.tvbs.com.tw/')
time.sleep(random.uniform(5, 10))
print(browser.title)

#靜態爬蟲思維
with open('d20260117_tvbs.csv','w',newline='') as f:
    writer=csv.writer(f)
    
    sp=BeautifulSoup(browser.page_source,'html.parser')
    datatag=sp.select('li a h2')
    for i in range(len(datatag)):
        print(datatag[i].text)
        writer.writerow([datatag[i].text])
                  
print("抓取成功")

