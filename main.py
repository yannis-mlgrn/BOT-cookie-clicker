from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

#import the web driver of google chrome
WEBDRIVER_PATH= 'bin/chromedriver'
driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH)
# load the clicker cookie page
driver.get('https://orteil.dashnet.org/cookieclicker/')

while True :

    # wait for loading and init of the web page
    wait = WebDriverWait(driver, 90)
    #wait until the cookie is clickable
    wait.until(expected_conditions.element_to_be_clickable((By.ID, "bigCookie")))

    # bot
    cookie = driver.find_element_by_id("bigCookie")
    cookie.click()


