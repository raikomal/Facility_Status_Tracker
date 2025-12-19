from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SliderPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_slider(self, slider_name):
        slider_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//button[normalize-space()='{slider_name}']")
            )
        )
        slider_button.click()
