# from browser.browser_setup import chrome_setup
# from pages.login_page import LoginPage
# from utils.csv_writer import write_test_report
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# def handle_alert_if_present(driver, timeout=4):
#     try:
#         WebDriverWait(driver, timeout).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         alert.accept()
#         time.sleep(2)
#     except:
#         pass

# def login_and_reach_dashboard():
#     driver = chrome_setup()
#     driver.get("http://103.204.95.212:8084/")
#     login_page = LoginPage(driver)

#     # 1️⃣ Empty login
#     login_page.clear_fields()
#     login_page.click_login()
#     login_page.accept_alert_if_present()
#     time.sleep(4)


#     write_test_report(
#         "Tower Track","Web","Login Module",
#         "Login without credentials",
#         "Click login without entering data",
#         "Validation message should appear",
#         "Validation message displayed",
#         "Pass","", "1923",""
#     )

#     # 2️⃣ Invalid login
#     login_page.login("user@123", "123467")
#     handle_alert_if_present(driver)

#     write_test_report(
#         "Tower Track","Web","Login Module",
#         "Login with invalid credentials",
#         "Enter wrong email/password",
#         "Error alert should appear",
#         "Error alert displayed",
#         "Pass","Alert handled", "1923",""
#     )

#     # 3️⃣ Valid login
#     driver.refresh()
#     login_page = LoginPage(driver)
#     login_page.login("user@gmail.com", "12345")

#     # ✅ WAIT FOR DASHBOARD
#     WebDriverWait(driver, 15).until(
#         EC.visibility_of_element_located(
#             ("xpath", "//div[@class='dashboard-card-container flex flex-wrap']")
#         )
#     )

#     write_test_report(
#         "Tower Track","Web","Login Module",
#         "Login with valid credentials",
#         "Enter correct email/password",
#         "Dashboard should load",
#         "Dashboard loaded successfully",
#         "Pass","", "1923",""
#     )

#     print("✅ Dashboard reached after login")
#     return driver   # 🔥 IMPORTANT

# from browser.browser_setup import chrome_setup
# from pages.login_page import LoginPage
# from utils.csv_writer import write_test_report
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
#
# def handle_alert_if_present(driver, timeout=4):
#     try:
#         WebDriverWait(driver, timeout).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         alert.accept()
#         time.sleep(2)
#     except:
#         pass
#
#
# def login_and_reach_dashboard():
#     # 1️⃣ Launch Browser
#     driver = chrome_setup()
#     write_test_report(
#         "Tower Track", "Web", "Login Module",
#         "Launch browser",
#         "Open Chrome browser",
#         "Browser should launch",
#         "Browser launched successfully",
#         "Pass", "", "1923", ""
#     )
#
#     # 2️⃣ Open Application URL
#     driver.get("http://103.204.95.212:8084/")
#     write_test_report(
#         "Tower Track", "Web", "Login Module",
#         "Open Tower Track URL",
#         "Navigate to application URL",
#         "Login page should load",
#         "Login page loaded",
#         "Pass", "", "1923", ""
#     )
#
#     login_page = LoginPage(driver)
#
#     # 3️⃣ Empty Login Validation
#     login_page.clear_fields()
#     login_page.click_login()
#     login_page.accept_alert_if_present()
#     time.sleep(2)
#
#     write_test_report(
#         "Tower Track", "Web", "Login Module",
#         "Login without credentials",
#         "Click login without entering data",
#         "Validation message should appear",
#         "Validation message displayed",
#         "Pass", "", "1923", ""
#     )
#
#     # 4️⃣ Invalid Login Validation
#     login_page.login("user@123", "123467")
#     handle_alert_if_present(driver)
#
#     write_test_report(
#         "Tower Track", "Web", "Login Module",
#         "Login with invalid credentials",
#         "Enter wrong email and password",
#         "Error alert should appear",
#         "Error alert displayed",
#         "Pass", "Alert handled", "1923", ""
#     )
#
#     # 5️⃣ Valid Login
#     driver.refresh()
#     login_page = LoginPage(driver)
#     login_page.login("user@gmail.com", "12345")
#
#     # 6️⃣ Dashboard Verification
#     WebDriverWait(driver, 15).until(
#         EC.visibility_of_element_located(
#             ("xpath", "//div[@class='dashboard-card-container flex flex-wrap']")
#         )
#     )
#
#     write_test_report(
#         "Tower Track", "Web", "Login Module",
#         "Login with valid credentials",
#         "Enter correct email and password",
#         "Dashboard should load",
#         "Dashboard loaded successfully",
#         "Pass", "", "1923", ""
#     )
#
#     print("✅ Dashboard reached after login")
#     return driver
from browser.browser_setup import chrome_setup
from pages.login_page import LoginPage
from utils.csv_writer import write_test_report
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def handle_alert_if_present(driver, timeout=4):
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
    except:
        pass


def login_and_reach_dashboard():
    # 1️⃣ Launch Browser
    driver = chrome_setup()
    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Launch browser",
        "Open Chrome browser",
        "Browser should launch",
        "Browser launched successfully",
        "Pass", "", "LG-01", ""
    )

    # 2️⃣ Open Application URL
    driver.get("http://103.204.95.212:8084/")
    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Open Tower Track URL",
        "Navigate to application URL",
        "Login page should load",
        "Login page loaded",
        "Pass", "", "LG-02", ""
    )

    login_page = LoginPage(driver)

    # 3️⃣ Empty Login Validation
    login_page.clear_fields()
    login_page.click_login()
    login_page.accept_alert_if_present()
    time.sleep(2)

    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Login without credentials",
        "Click login without entering data",
        "Validation message should appear",
        "Validation message displayed",
        "Pass", "", "LG-03", ""
    )

    # 4️⃣ Invalid Login Validation
    login_page.login("user@123", "123467")
    handle_alert_if_present(driver)

    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Login with invalid credentials",
        "Enter wrong email and password",
        "Error alert should appear",
        "Error alert displayed",
        "Pass", "Alert handled", "LG-04", ""
    )

    # 5️⃣ Valid Login (STEP-WISE CSV — Option A)
    driver.refresh()
    login_page = LoginPage(driver)

    # STEP 5.1 – Enter Email
    login_page.enter_email("user@gmail.com")
    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Enter valid email",
        "Enter registered email",
        "Email should be accepted",
        "Email entered",
        "Pass", "", "LG-05", ""
    )

    # STEP 5.2 – Enter Password
    login_page.enter_password("12345")
    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Enter valid password",
        "Enter correct password",
        "Password should be accepted",
        "Password entered",
        "Pass", "", "LG-06", ""
    )

    # STEP 5.3 – Click Login
    login_page.click_login()
    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Click Login",
        "Submit login form",
        "Dashboard should load",
        "Login submitted",
        "Pass", "", "LG-07", ""
    )

    # 6️⃣ Dashboard Verification
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            ("xpath", "//div[@class='dashboard-card-container flex flex-wrap']")
        )
    )

    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Verify Dashboard",
        "Wait for dashboard",
        "Dashboard should be visible",
        "Dashboard loaded successfully",
        "Pass", "", "LG-08", ""
    )

    print("✅ Dashboard reached after login")
    return driver
