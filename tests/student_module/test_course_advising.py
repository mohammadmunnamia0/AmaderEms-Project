import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("run", [1])
def test_course_advising(driver, run):
    wait = WebDriverWait(driver, 10)

    # Go to the course advising page
    driver.get("https://ems-test.amaderit.net/administer/Students/studentCourseAdvising")

    # Helper to select from dropdown with wait
    def select_dropdown(by_id, visible_text=None, index=None):
        wait.until(EC.presence_of_element_located((By.ID, by_id)))
        dropdown = Select(driver.find_element(By.ID, by_id))
        if visible_text:
            dropdown.select_by_visible_text(visible_text)
        elif index is not None:
            dropdown.select_by_index(index)

    # All dropdown selections
    dropdowns = {
        "campus_id": "BAF SEMC_jnu-2",
        "shift_id": "Morning",
        "medium_id": "English",
        "education_level_id": "Pre-Primary",
        "department_id": "Default",
        "class_name_id": "Play",
        "section_id": "Green",
        "session_id": "2024",
    }

    for field_id, visible_text in dropdowns.items():
        select_dropdown(field_id, visible_text=visible_text)

    # Select student (1st option excluding placeholder)
    select_dropdown("student_id", index=1)

    # Click on "Load Course" button
    load_course_btn = wait.until(EC.element_to_be_clickable((By.ID, "trigger-load-course")))
    load_course_btn.click()

    # Wait for course list or some table to appear (adjust selector if needed)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//table[contains(@class, 'table') or contains(text(), 'No Course Found')]")
        )
    )

    print("Course advising data loaded successfully.")
