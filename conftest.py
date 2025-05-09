import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.cookie_utils import save_cookies, load_cookies, get_cookie_file


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    # Setup with cross browser
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    # Make wait object available globally to test cases
    driver.wait = WebDriverWait(driver, timeout=10)

    # Navigate to site before loading cookies
    cookie_file = get_cookie_file(browser)
    base_url = "https://ems-test.amaderit.net/"

    driver.get(base_url)

    # Load cookies if available, else perform login
    if os.path.exists(cookie_file):
        load_cookies(driver, browser)
        driver.get(base_url)  # Reload to apply cookies
        if not is_logged_in(driver):
            perform_login_and_save_cookies(driver, browser)
    else:
        perform_login_and_save_cookies(driver, browser)

    yield driver

    # Capture screenshot on failure
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved to: {screenshot_path}")

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to attach test result information to the test item.
    Enables access to setup, call, and teardown results.
    """
    outcome = yield
    result = outcome.get_result()
    setattr(item, f"rep_{result.when}", result)


def login(driver, username: str, password: str):
    """
    Log in to the AmaderHR demo site using provided credentials.
    """
    driver.get("https://ems-test.amaderit.net/")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for a dashboard element to confirm login
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='message alert alert-success']"))
    )


def perform_login_and_save_cookies(driver, browser_name):
    login(driver, username="adming2", password="12345678")
    save_cookies(driver, browser_name)

def is_logged_in(driver) -> bool:
    """
    Check whether the user is logged in by waiting for a dashboard element.
    """
    try:
        driver.wait.until(
            EC.presence_of_element_located((
                By.XPATH, "//div[@class='message alert alert-success']"
            ))
        )
        return True
    except Exception:
        return False

