from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Login
driver.get("https://ems-test.amaderit.net/")
driver.find_element(By.ID, "username").send_keys("adming2")
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
time.sleep(2)

# Step 2: Navigate to Exam Template page
driver.get("https://ems-test.amaderit.net/administer/exam-templates")
time.sleep(2)

# Step 3: Click on "New Template" button
driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-xs']").click()
time.sleep(4)

# Step 4: Fill out the form fields
driver.find_element(By.ID, "examination_name").send_keys("Automation Test Template")
time.sleep(1)
Select(driver.find_element(By.ID, "campus_id")).select_by_visible_text("BAF SEMC_jnu-2")
time.sleep(1)
Select(driver.find_element(By.ID, "shift_id")).select_by_visible_text("Morning")
time.sleep(1)
Select(driver.find_element(By.ID, "medium_id")).select_by_visible_text("English")
time.sleep(1)
Select(driver.find_element(By.ID, "education_level_id")).select_by_visible_text("Pre-Primary")
time.sleep(3)
Select(driver.find_element(By.ID, "department_id")).select_by_visible_text("Default")
time.sleep(1)
Select(driver.find_element(By.ID, "session_id")).select_by_visible_text("2025")
time.sleep(1)
Select(driver.find_element(By.ID, "class_name_id")).select_by_visible_text("Nursery")
time.sleep(1)

# Step 5: Click Save
driver.find_element(By.XPATH, "//button[@type='submit']").click()


# Optional: Wait and close
time.sleep(3)
driver.quit()
