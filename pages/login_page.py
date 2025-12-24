from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username_input = "//input[@placeholder='Username or email']"
    password_input = "//input[@placeholder='Password']"
    login_button = "//button[normalize-space()='LOGIN']"

    def clear_fields(self):
        self.driver.find_element(By.XPATH, self.username_input).clear()
        self.driver.find_element(By.XPATH, self.password_input).clear()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def login(self, username, password):
        self.clear_fields()
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button).click()

    # ALERT HANDLING
    def accept_alert_if_present(self):
        try:
            myalert = self.driver.switch_to.alert
            print("Alert text:", myalert.text)
            myalert.accept()   # CLICK OK
            print(" Alert OK clicked")
        except NoAlertPresentException:
            pass
