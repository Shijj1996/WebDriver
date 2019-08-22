from selenium import webdriver
import time

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.baidu.com")
time.sleep(2)
driver.quit()

