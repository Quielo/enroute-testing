from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/")

driver.find_element(By.NAME, "userName").click()
driver.find_element(By.NAME, "userName").send_keys("user")
driver.find_element(By.NAME, "password").click()
driver.find_element(By.NAME, "password").send_keys("pass")
driver.find_element(By.NAME, "submit").click()