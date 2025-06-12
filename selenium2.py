from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Launch Chrome browser
driver = webdriver.Chrome()

# 2. Open Google
driver.get("https://www.googlechrome.com")

# 3. Find the search box
search_box = driver.find_element(By.NAME, "q")

# 4. Type in a search term and hit Enter
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# 5. Wait for results to load
time.sleep(2000)
