import time
from selenium import webdriver

driver = webdriver.Chrome()  
driver.get("https://www.flipkart.com/mobile-phones-store")
print("Page title is:", driver.title)
time.sleep(2000) 

