from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Launch Chrome browser
driver = webdriver.Chrome()

# 2. Go to the login page
driver.get("https://www.gmail.com/")

# 3. Find username and password fields and enter credentials
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# 4. Click the login button
driver.find_element(By.ID, "login-button").click()

# 5. Wait to see the result
time.sleep(2)

# 6. Verify login by checking for presence of a page element
if "inventory" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed!")

# 7. Close the browser
driver.quit()
