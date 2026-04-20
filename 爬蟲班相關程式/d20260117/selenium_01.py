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

browser.close()
browser.quit()

