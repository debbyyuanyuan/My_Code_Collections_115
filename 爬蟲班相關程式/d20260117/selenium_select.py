from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#啟動瀏覽器
#靜態選擇
browser=webdriver.Chrome()
browser.get('https://www.wibibi.com/info.php?tid=194')
selectA=Select(browser.find_element(By.NAME, "YourLocation"))
for option in selectA.options:
    print(option.text)
browser.close()


