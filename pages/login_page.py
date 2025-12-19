from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username_input = "//input[@placeholder='Username or email']"
    password_input = "//input[@placeholder='Password']"
    login_button = "//button[normalize-space()='LOGIN']"

    def login(self, username, password):
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button).click()
