# pages/part_allocation_home_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
import time


class PartAllocationHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # =================================================
    # BACK FROM IMPACT ANALYSIS → PART ALLOCATION HOME
    # =================================================
    def go_back_from_impact_to_home(self):
        """
        Click HomeMenu button and visibly return to Part Allocation cards
        """

        home_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//img[@alt='HomeMenu']")
            )
        )

        # Scroll to make it visible (demo-safe)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            home_btn
        )

        time.sleep(0.5)  # 👀 HUMAN-visible pause

        # JS click (SVG/image safe)
        self.driver.execute_script("arguments[0].click();", home_btn)

        # ⏳ WAIT for Part Allocation cards
        sla_card = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'SLA & Risk Heatmap')]")
            )
        )

        # Scroll to cards so tester sees them
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            sla_card
        )

        time.sleep(1.2)  # 👀 VERY IMPORTANT for demo

        print("✅ BACK BUTTON WORKED → Part Allocation cards visible")

    def hover_sla_risk_heatmap_card(self):
        card = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'SLA & Risk Heatmap')]")
            )
        )

        ActionChains(self.driver) \
            .move_to_element(card) \
            .pause(1) \
            .perform()

        print("🟢 Hovered on SLA & Risk Heatmap card")

    def open_sla_risk_heatmap(self):
        card = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(text(),'SLA & Risk Heatmap')]")
            )
        )

        self.driver.execute_script("arguments[0].click();", card)

        # Wait for SLA page indicator
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'SLA')]")
            )
        )

        time.sleep(1)

        print("✅ SLA & Risk Heatmap page opened")

