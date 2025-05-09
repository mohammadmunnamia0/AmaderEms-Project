from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
# driver.get("https://ems-test.amaderit.net/")  # Adjust if already logged in
#
# # Optional: login if needed
# driver.find_element(By.ID, "username").send_keys("adming2")
# driver.find_element(By.ID, "password").send_keys("12345678")
# driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
# time.sleep(2)

# Navigate to student list page
driver.get("https://ems-test.amaderit.net/administer/Students/index")
time.sleep(2)  # Wait for page load

# Select dropdown values (use actual values from your system)
Select(driver.find_element(By.ID, "campus_id")).select_by_visible_text("BAF SEMC_jnu-2")
time.sleep(2)
Select(driver.find_element(By.ID, "shift_id")).select_by_visible_text("Morning")
time.sleep(2)
Select(driver.find_element(By.ID, "medium_id")).select_by_visible_text("English")
time.sleep(2)
Select(driver.find_element(By.ID, "education_level_id")).select_by_visible_text("Pre-Primary")
time.sleep(2)
Select(driver.find_element(By.ID, "department_id")).select_by_visible_text("Default")
time.sleep(2)
Select(driver.find_element(By.ID, "class_name_id")).select_by_visible_text("Play")
time.sleep(2)
Select(driver.find_element(By.ID, "section_id")).select_by_visible_text("Orange")
time.sleep(2)
Select(driver.find_element(By.ID, "session_id")).select_by_visible_text("2025")
time.sleep(2)

# Click the "Load Student" button
driver.find_element(By.XPATH, "//button[@type='button']").click()

# Wait for student table to update (you can fine-tune this wait)
#WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((
#        By.XPATH,
#        "//table[@id='DataTables_Table_0']//tbody/tr | //td[contains(text(), 'No matching records')]"
#    ))
#)


driver.quit()
