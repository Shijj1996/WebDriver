from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
import time

fp=open("./baidu-sourcecode.txt",'w+')

chrome_opt=Options()
#chrome_opt.add_argument("--headless")
#chrome_opt.add_argument("--disable-gpu")
chrome_opt.add_argument("--window-size=800,400")
chrome_opt.add_argument("--disable-infobars")

driver=webdriver.Chrome("/usr/local/bin/chromedriver",chrome_options=chrome_opt)
driver.get("https://www.baidu.com")
time.sleep(2)
print(driver.page_source,file=fp)
driver.quit()
