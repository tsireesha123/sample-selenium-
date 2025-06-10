from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://gmail.com")  
driver.find_element(By.NAME, "txtUserName").send_keys("siri")
driver.find_element(By.NAME, "txtPassword").send_keys("siri")
driver.find_element(By.NAME, "submit").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "logout").click()
driver.close()
