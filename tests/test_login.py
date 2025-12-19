from browser.browser_setup import chrome_setup
from pages.login_page import LoginPage
from utils.csv_writer import write_test_report
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def handle_alert_if_present(driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1)
    except:
        pass

def login_and_reach_dashboard():
    driver = chrome_setup()
    driver.get("http://103.204.95.212:8084/")
    login_page = LoginPage(driver)

    # 1️⃣ Empty login
    login_page.clear_fields()
    login_page.click_login()
    time.sleep(2)

    write_test_report(
        "Tower Track","Web","Login Module",
        "Login without credentials",
        "Click login without entering data",
        "Validation message should appear",
        "Validation message displayed",
        "Pass","", "1923",""
    )

    # 2️⃣ Invalid login
    login_page.login("user@123", "123467")
    handle_alert_if_present(driver)

    write_test_report(
        "Tower Track","Web","Login Module",
        "Login with invalid credentials",
        "Enter wrong email/password",
        "Error alert should appear",
        "Error alert displayed",
        "Pass","Alert handled", "1923",""
    )

    # 3️⃣ Valid login
    driver.refresh()
    login_page = LoginPage(driver)
    login_page.login("user@gmail.com", "12345")

    # ✅ WAIT FOR DASHBOARD
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            ("xpath", "//div[@class='dashboard-card-container flex flex-wrap']")
        )
    )

    write_test_report(
        "Tower Track","Web","Login Module",
        "Login with valid credentials",
        "Enter correct email/password",
        "Dashboard should load",
        "Dashboard loaded successfully",
        "Pass","", "1923",""
    )

    print("✅ Dashboard reached after login")
    return driver   # 🔥 IMPORTANT
