import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


@pytest.mark.parametrize("run", [1])  # Ensures pytest collects the test
def test_course_advising(driver, run):  # driver fixture comes from conftest.py
    # Navigate directly to the course advising page (assuming cookies/login handled in conftest)
    driver.get("https://ems-test.amaderit.net/administer/Students/studentCourseAdvising")
    time.sleep(2)

    # Select dropdowns with some wait in between
    Select(driver.find_element(By.ID, "campus_id")).select_by_visible_text("BAF SEMC_jnu-2")
    time.sleep(1)
    Select(driver.find_element(By.ID, "shift_id")).select_by_visible_text("Morning")
    time.sleep(1)
    Select(driver.find_element(By.ID, "medium_id")).select_by_visible_text("English")
    time.sleep(1)
    Select(driver.find_element(By.ID, "education_level_id")).select_by_visible_text("Pre-Primary")
    time.sleep(1)
    Select(driver.find_element(By.ID, "department_id")).select_by_visible_text("Default")
    time.sleep(1)
    Select(driver.find_element(By.ID, "class_name_id")).select_by_visible_text("Play")
    time.sleep(1)
    Select(driver.find_element(By.ID, "section_id")).select_by_visible_text("Green")
    time.sleep(1)
    Select(driver.find_element(By.ID, "session_id")).select_by_visible_text("2024")
    time.sleep(2)

    # Select a student and click the "Show" button
    Select(driver.find_element(By.ID, "student_id")).select_by_index(1)
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[@id='trigger-load-course']").click()
    time.sleep(3)
