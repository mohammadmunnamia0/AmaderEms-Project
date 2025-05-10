import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dummy_student = {
    "full_en": "Sumaiya Chowdhury",
    "full_bn": "Sumaiya Chowdhury",
    "dob": "2009-01-09",
    "pin_number": "567202762",
    "birth_reg_no": "6747818141437",
    "email": "sumaiya.chowdhury@example.com",
    "phone": "01821097155",
    "father": "Karim Akter",
    "mother": "Rahim Hasan",
    "guardian": "Rahim Miah"
}

@pytest.mark.parametrize("run", [1])
def test_add_student(driver, run):
    wait = WebDriverWait(driver, 10)
    driver.get("https://ems-test.amaderit.net/administer/Students/add")

    def wait_and_type(by_id, text):
        wait.until(EC.presence_of_element_located((By.ID, by_id))).send_keys(text)

    def wait_and_select_text(by_id, text):
        wait.until(EC.presence_of_element_located((By.ID, by_id)))
        Select(driver.find_element(By.ID, by_id)).select_by_visible_text(text)

    def wait_and_select_index(by_id, index):
        wait.until(EC.presence_of_element_located((By.ID, by_id)))
        Select(driver.find_element(By.ID, by_id)).select_by_index(index)

    # Basic Info
    wait_and_type("pin_number", dummy_student["pin_number"])
    wait_and_type("full_name_en", dummy_student["full_en"])
    wait_and_type("full_name_bn", dummy_student["full_bn"])
    wait_and_type("birth_registration_no", dummy_student["birth_reg_no"])
    wait_and_type("dob", dummy_student["dob"])
    wait_and_type("nationality", "Bangladeshi")
    wait_and_select_text("country", "BANGLADESH")
    wait_and_select_text("religion", "Islam")
    wait_and_select_text("blood_group", "A+")
    wait_and_select_text("gender", "Female")
    wait_and_select_text("maritual_status", "Unmarried")
    wait_and_type("student_email", dummy_student["email"])
    wait_and_type("study_break_remarks", "No break taken.")

    # Family Info
    wait_and_type("father_name_en", dummy_student["father"])
    wait_and_type("father_contact_no", "01712345678")
    driver.find_element(By.ID, "father_also_guardian").click()
    wait_and_type("father_nid", "1234567890")
    wait_and_type("mother_name_en", dummy_student["mother"])
    wait_and_type("mother_contact_no", "01812345678")
    driver.find_element(By.ID, "mother_is_guardian").click()
    wait_and_type("mother_nid", "9876543210")
    wait_and_select_text("guardian_type", "Father")
    wait_and_type("local_guardian_name_en", dummy_student["guardian"])
    wait_and_type("local_guardian_contact_no", "01987654321")
    wait_and_type("local_guardian_relation", "Uncle")
    wait_and_type("student_contact", dummy_student["phone"])
    wait_and_type("father_occupation", "Businessman")
    wait_and_select_text("quota", "মুক্তিযোদ্ধা সন্তান")
    wait_and_type("father_yearly_income", "500000")

    # Address
    wait_and_type("present_address", "123 Example Street, Dhaka")
    wait_and_type("parmanent_address", "456 Permanent Rd, Chattogram")

    # Academic Info
    wait_and_select_index("campus_id", 1)
    wait_and_select_text("shift_id", "Morning")
    wait_and_select_text("medium_id", "English")
    wait_and_select_text("education_level_id", "Pre-Primary")
    wait_and_select_text("department_id", "Default")
    wait_and_select_text("class_name_id", "Play")
    wait_and_select_index("section_id", 1)
    wait_and_select_text("session_id", "2025")
    wait_and_type("roll", "23")
    wait_and_type("registration_number", "REG20240023")
    wait_and_type("attendance_machine_id", "AM20240023")
    wait_and_type("addmission_date", "2024-01-10")
    wait_and_select_text("student_category", "Civil")
    wait_and_type("old_student_code", "OLD2023STU")

    # Academic Qualifications
    for i in range(3):
        wait_and_type(f"edu_division_{i}", "Dhaka")
        wait_and_type(f"edu_roll_number_{i}", f"ROLL202{i}")
        wait_and_type(f"edu_gpa_{i}", "5.00")
        wait_and_type(f"edu_passing_year_{i}", f"20{20+i}")
        wait_and_type(f"edu_registration_number_{i}", f"REG202{i}0")
        wait_and_type(f"edu_session_{i}", f"20{19+i}-20{20+i}")
        wait_and_type(f"edu_board_{i}", "Dhaka")

    # Hostel & Transport
    wait_and_select_text("hostel_id", "Uttara Hostel")
    wait_and_select_index("hostel_room_id", 1)
    wait_and_type("allotment_date", "2024-02-01")
    wait_and_type("transport_bus_no", "202")
    wait_and_type("transport_road_no", "406")

    # Submit
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()

    # Assertion: Confirm student creation
    assert "Student" in driver.title or "successfully" in driver.page_source
