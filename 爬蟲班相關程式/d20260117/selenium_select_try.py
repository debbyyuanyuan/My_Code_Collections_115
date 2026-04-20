from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

#啟動瀏覽器
#靜態選擇
browser=webdriver.Chrome()
browser.get('https://www.twse.com.tw/zh/trading/historical/mi-5mins.html')
selectA=Select(browser.find_element(By.NAME, "yy"))
selectB=Select(browser.find_element(By.NAME, "mm"))
selectC=Select(browser.find_element(By.NAME, "dd"))

#點選指定年月份
selectA.select_by_visible_text('民國 112 年')
selectB.select_by_visible_text('02月')
selectC.select_by_visible_text('06日 (一)')
time.sleep(random.uniform(5,10))

#<button class="search">查詢<button>
selectBB=browser.find_element(By.CLASS_NAME, "search")

#點擊按鈕
selectBB.click()
time.sleep(random.uniform(10,20))
input("按下enter鍵已結束程式並關閉瀏覽器")
browser.quit()
#browser.close()