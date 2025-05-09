import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

@pytest.mark.parametrize("run", [1])  # Helps pytest collect this test
def test_add_student(driver,run):  # <-- use fixture from conftest.py
    driver.get("https://ems-test.amaderit.net/administer/Students/add")
    time.sleep(1)

    driver.find_element(By.ID, "pin_number").send_keys(dummy_student["pin_number"])
    driver.find_element(By.ID, "full_name_en").send_keys(dummy_student["full_en"])
    driver.find_element(By.ID, "full_name_bn").send_keys(dummy_student["full_bn"])
    driver.find_element(By.ID, "birth_registration_no").send_keys(dummy_student["birth_reg_no"])
    driver.find_element(By.ID, "dob").send_keys(dummy_student["dob"])
    driver.find_element(By.ID, "nationality").send_keys("Bangladeshi")
    Select(driver.find_element(By.ID, "country")).select_by_visible_text("BANGLADESH")
    Select(driver.find_element(By.ID, "religion")).select_by_visible_text("Islam")
    Select(driver.find_element(By.ID, "blood_group")).select_by_visible_text("A+")
    Select(driver.find_element(By.ID, "gender")).select_by_visible_text("Female")
    Select(driver.find_element(By.ID, "maritual_status")).select_by_visible_text("Unmarried")
    driver.find_element(By.ID, "student_email").send_keys(dummy_student["email"])

    # driver.find_element(By.ID, "profile_picture").send_keys(
    #     r"C:\Users\tonmo\Downloads\b2b76ce53754fbb3442f994450240d5d.jpg"
    # )

    driver.find_element(By.ID, "study_break_remarks").send_keys("No break taken.")

    # Family Info
    driver.find_element(By.ID, "father_name_en").send_keys(dummy_student["father"])
    driver.find_element(By.ID, "father_contact_no").send_keys("01712345678")
    driver.find_element(By.ID, "father_also_guardian").click()
    driver.find_element(By.ID, "father_nid").send_keys("1234567890")
    driver.find_element(By.ID, "mother_name_en").send_keys(dummy_student["mother"])
    driver.find_element(By.ID, "mother_contact_no").send_keys("01812345678")
    driver.find_element(By.ID, "mother_is_guardian").click()
    driver.find_element(By.ID, "mother_nid").send_keys("9876543210")
    Select(driver.find_element(By.ID, "guardian_type")).select_by_visible_text("Father")
    driver.find_element(By.ID, "local_guardian_name_en").send_keys(dummy_student["guardian"])
    driver.find_element(By.ID, "local_guardian_contact_no").send_keys("01987654321")
    driver.find_element(By.ID, "local_guardian_relation").send_keys("Uncle")
    driver.find_element(By.ID, "student_contact").send_keys(dummy_student["phone"])
    driver.find_element(By.ID, "father_occupation").send_keys("Businessman")
    Select(driver.find_element(By.ID, "quota")).select_by_visible_text("মুক্তিযোদ্ধা সন্তান")
    driver.find_element(By.ID, "father_yearly_income").send_keys("500000")

    driver.find_element(By.ID, "present_address").send_keys("123 Example Street, Dhaka")
    driver.find_element(By.ID, "parmanent_address").send_keys("456 Permanent Rd, Chattogram")
    time.sleep(3)
    # Academic Info
    Select(driver.find_element(By.ID, "campus_id")).select_by_index(1)
    time.sleep(2)
    Select(driver.find_element(By.ID, "shift_id")).select_by_visible_text("Morning")
    Select(driver.find_element(By.ID, "medium_id")).select_by_visible_text("English")
    time.sleep(2)
    Select(driver.find_element(By.ID, "education_level_id")).select_by_visible_text("Pre-Primary")
    time.sleep(2)
    Select(driver.find_element(By.ID, "department_id")).select_by_visible_text("Default")
    time.sleep(2)
    Select(driver.find_element(By.ID, "class_name_id")).select_by_visible_text("Play")
    time.sleep(2)
    Select(driver.find_element(By.ID, "section_id")).select_by_index(1)
    time.sleep(2)
    Select(driver.find_element(By.ID, "session_id")).select_by_visible_text("2025")
    driver.find_element(By.ID, "roll").send_keys("23")
    driver.find_element(By.ID, "registration_number").send_keys("REG20240023")
    driver.find_element(By.ID, "attendance_machine_id").send_keys("AM20240023")
    driver.find_element(By.ID, "addmission_date").send_keys("2024-01-10")
    Select(driver.find_element(By.ID, "student_category")).select_by_visible_text("Civil")
    driver.find_element(By.ID, "old_student_code").send_keys("OLD2023STU")

    # Academic Qualifications
    for i in range(3):
        driver.find_element(By.ID, f"edu_division_{i}").send_keys("Dhaka")
        driver.find_element(By.ID, f"edu_roll_number_{i}").send_keys(f"ROLL202{i}")
        driver.find_element(By.ID, f"edu_gpa_{i}").send_keys("5.00")
        driver.find_element(By.ID, f"edu_passing_year_{i}").send_keys(f"20{20+i}")
        driver.find_element(By.ID, f"edu_registration_number_{i}").send_keys(f"REG202{i}0")
        driver.find_element(By.ID, f"edu_session_{i}").send_keys(f"20{19+i}-20{20+i}")
        driver.find_element(By.ID, f"edu_board_{i}").send_keys("Dhaka")

    # Hostel & Transport
    Select(driver.find_element(By.ID, "hostel_id")).select_by_visible_text("Uttara Hostel")
    time.sleep(1)
    Select(driver.find_element(By.ID, "hostel_room_id")).select_by_index(1)
    driver.find_element(By.ID, "allotment_date").send_keys("2024-02-01")

    driver.find_element(By.ID, "transport_bus_no").send_keys("202")
    driver.find_element(By.ID, "transport_road_no").send_keys("406")

    # Save
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(3)

    # Basic assertion to verify redirection
    assert "Student" in driver.title or "successfully" in driver.page_source
