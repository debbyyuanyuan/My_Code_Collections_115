#避免瀏覽器出現機器人驗證
# pip install undetected-chromedriver

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# 直接用 undetected_chromedriver
browser = uc.Chrome()
browser.get('https://www.google.com.tw')
time.sleep(random.uniform(3, 6))

inputA = browser.find_element(By.NAME, 'q')
for char in '近期草莓價格':
    inputA.send_keys(char)
    time.sleep(random.uniform(0.05, 0.25))

inputA.send_keys(Keys.ENTER)
time.sleep(random.uniform(5, 10))

print(browser.title)
# browser.quit()