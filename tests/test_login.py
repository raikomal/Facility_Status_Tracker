from browser.browser_setup import chrome_setup
from pages.login_page import LoginPage
from utils.csv_writer import write_result
import time

def test_login():
    driver = chrome_setup()
    driver.get("http://103.204.95.212:8084/")

    try:
        login_page = LoginPage(driver)
        login_page.login("user@gmail.com", "12345")

        time.sleep(5)  # later replace with WebDriverWait
        write_result("Login Test", "PASS", "Login successful")

    except Exception as e:
        write_result("Login Test", "FAIL", str(e))

    finally:
        driver.quit()
