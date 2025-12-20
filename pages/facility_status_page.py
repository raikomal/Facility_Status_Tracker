from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver import ActionChains
import time



class FacilityStatusPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # =========================================================
    # STRATEGIC OVERVIEW TAB
    # =========================================================
    STRATEGIC_OVERVIEW = (
        By.XPATH, "//button[normalize-space()='Strategic Overview']"
    )

    STRATEGIC_OVERVIEW_TEXT = (
        By.XPATH, "//*[contains(text(),'Overall Fulfillment Rate')]"
    )

    # =========================================================
    # MAP LOCATORS (STABLE FOR HIGHCHARTS MAP)
    # =========================================================
    MAP_CONTAINER = (By.CSS_SELECTOR, "svg.highcharts-root")

    # Only interactive map points (exclude background paths)
    FACILITY_POINTS = (
        By.CSS_SELECTOR,
        "path.highcharts-point, path.highcharts-map-point"
    )

    TOOLTIP = (By.CSS_SELECTOR, "g.highcharts-tooltip")

    # =========================================================
    # ACTIONS
    # =========================================================
    def click_strategic_overview(self):
        self.wait.until(
            EC.element_to_be_clickable(self.STRATEGIC_OVERVIEW)
        ).click()

    def verify_strategic_overview_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(self.STRATEGIC_OVERVIEW_TEXT)
        )
        return True

    # =========================================================
    # MAP – BASIC VISIBILITY
    # =========================================================
    def verify_map_visible(self):
        """
        Wait until Highcharts SVG AND at least one point is present
        """
        # Wait for SVG container
        self.wait.until(
            EC.presence_of_element_located(self.MAP_CONTAINER)
        )

        # Wait until at least one facility point is present
        self.wait.until(
            lambda driver: len(self.get_facility_points()) > 0
        )

        return True

    def get_facility_points(self):
        """
        Return all interactive facility points on map
        """
        return self.driver.find_elements(*self.FACILITY_POINTS)

    # =========================================================
    # MAP – ONE FACILITY HOVER
    # =========================================================
    def hover_on_first_facility(self):
        """
        Hover on first real facility point
        """
        self.verify_map_visible()

        points = self.get_facility_points()

        if not points:
            raise Exception("No interactive facility points found on map")

        ActionChains(self.driver)\
            .move_to_element(points[0])\
            .pause(0.5)\
            .perform()

    def is_tooltip_visible(self):
        """
        Verify tooltip appears after hover
        """
        self.wait.until(
            EC.visibility_of_element_located(self.TOOLTIP)
        )
        return True

    def hover_on_specific_facility(self, element):
        """
        Hover on a single facility point
        """
        ActionChains(self.driver) \
            .move_to_element(element) \
            .pause(0.5) \
            .perform()

    def hover_on_multiple_facilities(self, count=4):
        """
        Hover on first `count` facility points one by one
        """
        self.verify_map_visible()

        points = self.get_facility_points()

        max_points = min(count, len(points))

        for i in range(max_points):
            self.hover_on_specific_facility(points[i])
            time.sleep(1.5)
