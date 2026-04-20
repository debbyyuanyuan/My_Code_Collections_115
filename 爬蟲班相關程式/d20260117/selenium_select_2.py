from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

#啟動瀏覽器
#靜態選擇
browser=webdriver.Chrome()
browser.get('https://www.wibibi.com/info.php?tid=194')
selectA=Select(browser.find_element(By.NAME, "YourLocation"))
selectA.select_by_visible_text('新竹')
time.sleep(random.uniform(5,10))
browser.quit()
#browser.close()