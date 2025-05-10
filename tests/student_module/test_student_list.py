from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize browser
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Step 1: Navigate to student list page
driver.get("https://ems-test.amaderit.net/administer/Students/index")

# Helper function to select dropdown by visible text
def select_dropdown(by_id, visible_text):
    wait.until(EC.presence_of_element_located((By.ID, by_id)))
    Select(driver.find_element(By.ID, by_id)).select_by_visible_text(visible_text)

# Step 2: Select dropdown values with proper waiting
dropdowns = {
    "campus_id": "BAF SEMC_jnu-2",
    "shift_id": "Morning",
    "medium_id": "English",
    "education_level_id": "Pre-Primary",
    "department_id": "Default",
    "class_name_id": "Play",
    "section_id": "Orange",
    "session_id": "2025"
}

for key, value in dropdowns.items():
    select_dropdown(key, value)

# Step 3: Click the "Load Student" button (make sure it's the right one)
load_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(text(),'Load Student')]")))
load_button.click()

# Step 4: Wait for table to load or show "No matching records"
wait.until(
    EC.any_of(
        EC.presence_of_element_located((By.XPATH, "//table[@id='DataTables_Table_0']//tbody/tr")),
        EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'No matching records')]"))
    )
)

print("Student list loaded.")

# Done
driver.quit()
