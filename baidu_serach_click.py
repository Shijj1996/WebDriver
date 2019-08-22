from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("http://www.baidu.com")
print("1:",driver.title)
elem = driver.find_element_by_id("kw")
elem.send_keys("weibo")
elem.send_keys(Keys.RETURN)
time.sleep(2)

print("2:",driver.title)

elem =driver.find_element_by_link_text("weibo")
ActionChains(driver).move_to_element(elem).click().perform()
#ActionChains(driver).move_by_offset(200,150).click().perform()

time.sleep(4)

driver.close()