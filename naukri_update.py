from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# ---- USER CONFIG ----
NAUKRI_EMAIL = "your-email@gmail.com"
NAUKRI_PASSWORD = "your-password"
RESUME_PATH = r"your-resume-location-on-local.pdf" # change to your resume file path
# ---------------------

def update_naukri():
    # Open Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Go to Naukri login
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(2)

    # Enter login details
    driver.find_element(By.ID, "usernameField").send_keys(NAUKRI_EMAIL)
    driver.find_element(By.ID, "passwordField").send_keys(NAUKRI_PASSWORD)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)

    # Go to resume upload page
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    # Upload resume
    upload_btn = driver.find_element(By.XPATH, "//input[@id='attachCV']")
    upload_btn.send_keys(RESUME_PATH)
    time.sleep(5)

    print("✅ Resume updated successfully!")

    driver.quit()

if __name__ == "__main__":
    update_naukri()

