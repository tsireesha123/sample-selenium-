from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome Driver
driver = webdriver.Chrome()

# Open Flipkart
driver.get("https://www.flipkart.com")
driver.maximize_window()

# Wait for popup and close it
try:
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
    )
    close_button.click()
except:
    print("No login popup appeared.")

# Wait for search box and enter product name
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(5)

# Optionally, scrape first product title
titles = driver.find_elements(By.CLASS_NAME, "_4rR01T")
if titles:
    print("First product title:", titles[0].text)
else:
    print("No products found.")

# Close the browser
driver.quit()
