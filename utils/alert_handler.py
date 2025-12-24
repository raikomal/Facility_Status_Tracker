from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def handle_any_alert(driver, timeout=3):
    try:
        alert = WebDriverWait(driver, timeout).until(EC.alert_is_present())
        print(f"Alert text: {alert.text}")
        alert.accept()
        print("Alert OK clicked")
    except TimeoutException:
        pass
