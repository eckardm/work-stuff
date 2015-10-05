'''
import what we need'''

# selenium is used automate web browser interaction, you'll need to install it
from selenium import webdriver

from thesearenotpasswords import *


'''
preliminaries'''

michigan_register = '1076099250'
mirlyn_catalog = 'http://mirlyn.lib.umich.edu/Record/000048789/Holdings#0'

'''
login to hathitrust'''

# setup web driver
driver = webdriver.Firefox()

# login
driver.get('https://weblogin.umich.edu/?cosign-babel.hathitrust.org&https://babel.hathitrust.org/cgi/ping/pong?target=https://www.hathitrust.org/')
driver.find_element_by_id('login').send_keys(login_id)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('loginSubmit').click()

# go to catalog record
driver.get('http://mirlyn.lib.umich.edu/Record/000048789/#0')
links = driver.find_elements_by_link_text('Full text')

# go through the links
for link in links:
    link.click()
    aw = driver.window_handles
    print aw
    driver.switch_to_window(aw[1])
    driver.find_element_by_xpath("//select[@id='PTaddItemSelect']/option[@value='1076099250']").click()
    driver.find_element_by_id('PTaddItemBtn').click()
    