from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

WEBDRIVER_PATH= 'bin/chromedriver'
driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH)
# suite
driver.get('https://orteil.dashnet.org/cookieclicker/')
# sleep(15)

# attendre fin du chargement et init de la page web
wait = WebDriverWait(driver, 90)
wait.until(expected_conditions.element_to_be_clickable((By.ID, "bigCookie")))

# suite

while True :
	cookie = driver.find_element_by_id("bigCookie")
	cookie.click()

	# récupération du compteur de cookies
	cookieNum = driver.find_element_by_id("cookies")
	print("cookies: ", cookieNum.text)


