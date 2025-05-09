from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

#Step 1: Login
driver.get("https://ems-test.amaderit.net/")
driver.find_element(By.ID, "username").send_keys("adming2")
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "logo")))
time.sleep(3)
# Step 2: Go to Exam Create page
driver.get("https://ems-test.amaderit.net/administer/temp-exam-masters/add")
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-success btn-xs']"))).click()
# time.sleep(1)
# Step 3: Fill the Exam Form
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "campus_id")))
Select(driver.find_element(By.ID, "campus_id")).select_by_index(1)
time.sleep(1)
Select(driver.find_element(By.ID, "shift_id")).select_by_visible_text("Morning")
time.sleep(1)
Select(driver.find_element(By.ID, "medium_id")).select_by_visible_text("English")
time.sleep(1)
Select(driver.find_element(By.ID, "education_level_id")).select_by_visible_text("Pre-Primary")
time.sleep(1)
Select(driver.find_element(By.ID, "department_id")).select_by_visible_text("Default")
time.sleep(1)  # Allow class dropdown to populate
Select(driver.find_element(By.ID, "class_name_id")).select_by_visible_text("Play")
time.sleep(1)
Select(driver.find_element(By.ID, "section_id")).select_by_index(1)
Select(driver.find_element(By.ID, "session_id")).select_by_visible_text("2025")

# Fill exam details
Select(driver.find_element(By.ID, "exam_type_id")).select_by_visible_text("Mid exam")  # Use your actual option
Select(driver.find_element(By.ID, "template_id")).select_by_visible_text("Mid")        # Use your actual template
driver.find_element(By.ID, "exam_name").send_keys("Automated Mid Term")
driver.find_element(By.ID, "exam_start_date").send_keys("2025-06-01")
driver.find_element(By.ID, "exam_end_date").send_keys("2025-06-15")
Select(driver.find_element(By.NAME, "result_process_type")).select_by_visible_text("New")
Select(driver.find_element(By.NAME, "marksheet_template_type")).select_by_visible_text("Pre Class")

# Submit the form
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait and finish
time.sleep(3)
print("Exam created successfully!")
driver.quit()
