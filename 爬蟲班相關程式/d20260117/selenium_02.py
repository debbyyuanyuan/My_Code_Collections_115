from selenium import webdriver
from selenium.webdriver.common.by import By
import time #讓模擬器有等待時間
import requests 
from bs4 import BeautifulSoup
import csv

#啟動Chrome瀏覽器
browser=webdriver.Chrome()
browser.get('https://www.google.com')
time.sleep(3)
#inputA=browser.find_element_by_name('q') #舊版寫法
inputA=browser.find_element(By.NAME,'q')
inputA.send_keys('雲林科技大學')
time.sleep(2)
inputA.submit()

#靜態爬蟲思維
sp=BeautifulSoup(browser.page_source,'html.parser')
#browser.close()
#browser.quit()

