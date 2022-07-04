from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import time
import csv

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

driver.get("https://www.sportovisteznojmo.cz/mestska-plovarna-louka")

time.sleep(5) # kód počká než se načte cookies

agree = driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/a")[0]

agree.click()



while True:
	visitors = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section/div/div/div[7]/div/div[1]/div/div/div/div/div/div")

	water_temperature = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section/div/div/div[7]/div/div[2]/div/div/div/div/div/div")

	temperature = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/big/strong")

	# Zjištění aktuálního času

	time_object = time.localtime()
	current_time = time.strftime("%d %m %a %H:%M", time_object)

	data_object = [current_time, visitors.text, water_temperature.text, temperature.text]

	# Zapisování do cvs souboru

	file = open("data.csv", "a", newline="")

	writer = csv.writer(file) 
	writer.writerow(data_object)

	file.close()

	time.sleep(600)

	driver.get(driver.current_url)
	time.sleep(2)
	driver.refresh()
	
driver.close()
