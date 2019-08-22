from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("http://www.baidu.com")
print("1:",driver.title)
elem = driver.find_element_by_id("kw")
elem.send_keys("weibo")
elem.send_keys(Keys.RETURN)
time.sleep(2)
print("2:",driver.title)
elem = driver.find_element_by_link_text(u"微博").click()

#print("url:",url)
#driver.get(url)

#elem.click()

'''
#assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
'''
time.sleep(4)

driver.close()