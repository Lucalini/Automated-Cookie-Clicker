from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
chrome_driver_path = "C:/Users/evasa/Documents/chromedriver.exe"
game_run = True

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

money = driver.find_element(By.ID, 'money')
cookie = driver.find_element(By.ID, 'cookie')

test = 1000
five_min = time.time() + (60 * 5)

while True:
    cookie.click()
    test -= 1
    if test == 0:
        try:
            driver.find_element(By.XPATH, '//*[@id="buyShipment"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyMine"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyFactory"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyGrandma"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyCursor"]').click()
        except:
            pass
        test = 1000

