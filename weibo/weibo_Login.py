from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

qqid='1025390513' 
qqpwd='140706wrh'

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("http://www.weibo.com")
time.sleep(6)
print("1:",driver.title)
#elem = driver.find_element_by_css_selector('a[node-type="loginBtn"]').click()
driver.find_element_by_css_selector('a[class="cp_logo icon_qq"]').click()
time.sleep(2)
print('2:',driver.title)
time.sleep(4)
driver.switch_to.window(driver.window_handles[1])
print('3:',driver.title)
driver.switch_to.frame('ptlogin_iframe')
driver.find_element_by_id('switcher_plogin').click()
time.sleep(2)
driver.find_element_by_id('u').send_keys(qqid)
driver.find_element_by_id('p').send_keys(qqpwd)
driver.find_element_by_id('login_button').click()
time.sleep(4)
driver.switch_to_default_content()



'''
elem = driver.find_element_by_css_selector('input[node-type="username"]').send_keys('15151830793')
elem = driver.find_element_by_css_selector('input[node-type="password"]').send_keys('sjj102539')
elem = driver.find_element_by_css_selector('a[action-type="btn_submit"]').click()
'''
time.sleep(2)