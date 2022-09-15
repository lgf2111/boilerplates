# Main Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Wait Imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Interraction Imports
from selenium.webdriver.common.by import By


# Install Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Driver must close in the end
try:
    driver.get("https://example.com/")

    # Wait for element
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a"))
        )
    except TimeoutException:
        driver.close()

    # Interract with element
    href = driver.find_element(By.CSS_SELECTOR, "a")
    href.click()


# Close driver
finally:
    driver.close()
