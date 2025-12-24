# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains


# class FacilityStatusPage:
#     DEMO_MODE = True
#     DEMO_DELAY = 3

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 40)

#     # ---------------- DEMO CONTROL ----------------
#     def demo_pause(self, multiplier=1):
#         time.sleep(self.DEMO_DELAY * multiplier)

#     # =========================================================
#     # STRATEGIC OVERVIEW
#     # =========================================================
#     def click_strategic_overview(self):
#         self.wait.until(
#             EC.element_to_be_clickable(
#                 (By.XPATH, "//button[normalize-space()='Strategic Overview']")
#             )
#         ).click()

#     def verify_strategic_overview_loaded(self):
#         self.wait.until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//*[name()='path' and contains(@class,'highcharts-point')]")
#             )
#         )
#         return True

# # =========================================================
# # MAP – STATUS OF ALL FACILITIES
# # =========================================================

# def get_facility_map_points(self):
#     """
#     Returns all Highcharts map circles (facility points)
#     """
#     self.wait.until(
#         EC.presence_of_element_located(
#             (By.XPATH, "//*[name()='path' and contains(@class,'highcharts-point')]")
#         )
#     )
#     return self.driver.find_elements(
#         By.XPATH, "//*[name()='path' and contains(@class,'highcharts-point')]"
#     )


# def hover_on_map_point(self, point):
#     """
#     Hover single map circle
#     """
#     ActionChains(self.driver).move_to_element(point).pause(0.5).perform()


# def hover_multiple_map_circles(self, count=5):
#     """
#     Demo-friendly map hover:
#     - picks 4–5 circles
#     - 0.5s pause between
#     """
#     points = self.get_facility_map_points()

#     if not points:
#         return False

#     count = min(count, len(points))

#     for p in points[:count]:
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", p
#         )
#         ActionChains(self.driver).move_to_element(p).pause(0.5).perform()

#     return True



# # def get_facility_map_points(self):
# #     return self.driver.find_elements(
# #         By.XPATH, "//*[name()='path' and contains(@class,'highcharts-point')]"
# #     )

# # def hover_on_map_point(self, point):
# #     """
# #     Single map hover (used by old tests)
# #     """
# #     ActionChains(self.driver).move_to_element(point).pause(1).perform()


# # # 🔥 NEW METHOD — CLIENT DEMO SAFE
# # def hover_multiple_map_circles(self, count=5):
# #     """
# #     Hover 4–5 random facility circles
# #     0.5s gap → realistic demo
# #     """
# #     import random

# #     circles = self.wait.until(
# #         EC.presence_of_all_elements_located(
# #             (
# #                 By.XPATH,
# #                 "//div[contains(@id,'highcharts')]//*[name()='path' and contains(@class,'highcharts-point')]"
# #             )
# #         )
# #     )

# #     if not circles:
# #         return False

# #     count = min(count, len(circles))
# #     selected = random.sample(circles, count)

# #     for circle in selected:
# #         self.driver.execute_script(
# #             "arguments[0].scrollIntoView({block:'center'});", circle
# #         )
# #         ActionChains(self.driver) \
# #             .move_to_element(circle) \
# #             .pause(0.5) \
# #             .perform()

# #     return True


#     # =========================================================
#     # KPI TABLE
#     # =========================================================
#     def scroll_to_kpi_table(self):
#         row = self.wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, "//tr[contains(@class,'font-semibold')]")
#             )
#         )
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", row
#         )

#     def get_all_kpi_facilities(self):
#         rows = self.wait.until(
#             EC.presence_of_all_elements_located(
#                 (By.XPATH, "//tbody//td[1]")
#             )
#         )
#         return [r.text.strip() for r in rows if r.text.strip()]
    
#     def demo_hover_kpi_table_rows(self, count=5):
#      facilities = self.get_all_kpi_facilities()

#     if not facilities:
#         return False

#     count = min(count, len(facilities))

#     for facility in facilities[:count]:
#         cell = self.wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, f"//td[normalize-space()='{facility}']")
#             )
#         )
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", cell
#         )
#         ActionChains(self.driver).move_to_element(cell).pause(0.5).perform()

#     return True




#     # def hover_on_kpi_row(self, facility):
#     #     cell = self.wait.until(
#     #         EC.visibility_of_element_located(
#     #             (By.XPATH, f"//td[normalize-space()='{facility}']")
#     #         )
#     #     )
#     #     ActionChains(self.driver).move_to_element(cell).pause(1).perform()




#     # =========================================================
#     # KPI BAR CHART
#     # =========================================================
#     def switch_kpi_view(self, view="barchart"):
#         dropdown = self.wait.until(
#             EC.presence_of_element_located(
#                 (
#                     By.XPATH,
#                     "//h2[normalize-space()='Facility KPIs']/following::select[1]"
#                 )
#             )
#         )
#         Select(dropdown).select_by_value(view)
#         self.demo_pause(2)

#     # def get_kpi_bars(self):
#     #     """
#     #     Return ONLY KPI bar chart bars (scoped to Facility KPIs section)
#     #     """
#     #     return self.wait.until(
#     #         EC.presence_of_all_elements_located(
#     #             (
#     #                 By.XPATH,
#     #                 "//h2[normalize-space()='Facility KPIs']"
#     #                 "/ancestor::div[contains(@class,'rounded')]"
#     #                 "//*[name()='path' and contains(@class,'highcharts-point')]"
#     #             )
#     #         )
#     #     )

#     def get_kpi_bars(self):
#      """
#     Return ONLY KPI bar chart bars (scoped & stable)
#      """
#     # Wait until KPI section is visible (IMPORTANT)
#     self.wait.until(
#         EC.visibility_of_element_located(
#             (By.XPATH, "//h2[normalize-space()='Facility KPIs']")
#         )
#     )

#     return self.wait.until(
#         EC.presence_of_all_elements_located(
#             (
#                 By.XPATH,
#                 "//h2[normalize-space()='Facility KPIs']"
#                 "/ancestor::div[contains(@class,'rounded')]"
#                 "//*[name()='path' and contains(@class,'highcharts-point')]"
#             )
#         )
#     )


#     # def hover_kpi_bar_by_index(self, index=0):
#     #     """
#     #     SAFE KPI bar hover:
#     #     - isolate KPI chart
#     #     - scroll into view
#     #     - re-fetch bars every time
#     #     """
#     #     bars = self.get_kpi_bars()

#     #     if not bars or index >= len(bars):
#     #         return False

#     #     bar = bars[index]

#     #     # Move viewport away from map
#     #     self.driver.execute_script(
#     #         "arguments[0].scrollIntoView({block:'center'});", bar
#     #     )
#     #     self.demo_pause(1)

#     #     ActionChains(self.driver) \
#     #         .move_to_element(bar) \
#     #         .move_by_offset(3, 3) \
#     #         .pause(1) \
#     #         .perform()

#     #     return True

#     def hover_kpi_bar_by_index(self, index=0):
#      """
#     SAFE KPI bar hover:
#     - isolate KPI chart
#     - scroll into view
#     - re-fetch bars every time
#      """
#     bars = self.get_kpi_bars()

#     if not bars or index >= len(bars):
#         return False

#     bar = bars[index]

#     self.driver.execute_script(
#         "arguments[0].scrollIntoView({block:'center'});", bar
#     )
#     self.demo_pause(0.5)

#     ActionChains(self.driver) \
#         .move_to_element(bar) \
#         .move_by_offset(3, 3) \
#         .pause(0.6) \
#         .perform()

#     return True


#     # =========================================================
#     # DISTRIBUTOR → FACILITY FLOW (SANKEY)
#     # =========================================================
#     def select_distributor_facility(self, value):
#         dropdown = self.wait.until(
#             EC.presence_of_element_located(
#                 (
#                     By.XPATH,
#                     "//h2[contains(text(),'Distributor')]/following::select[1]"
#                 )
#             )
#         )
#         Select(dropdown).select_by_visible_text(value)
#         self.demo_pause(2)

#     def get_flow_links(self):
#         return self.driver.find_elements(
#             By.XPATH, "//*[name()='path' and contains(@class,'highcharts-link')]"
#         )

#     def hover_flow_links(self):
#         links = self.get_flow_links()
#         for link in links[:5]:
#             ActionChains(self.driver).move_to_element(link).pause(1).perform()

#     # =========================================================
#     # FACILITY STATUS READINESS SUMMARY
#     # =========================================================
#     def select_readiness_view(self, value):
#         dropdown = self.wait.until(
#             EC.presence_of_element_located(
#                 (
#                     By.XPATH,
#                     "//h2[contains(text(),'Readiness')]/following::select[1]"
#                 )
#             )
#         )
#         Select(dropdown).select_by_visible_text(value)
#         self.demo_pause(2)

#     def get_readiness_bars(self):
#         return self.wait.until(
#             EC.presence_of_all_elements_located(
#                 (
#                     By.XPATH,
#                     "//div[contains(text(),'Readiness')]//*[name()='rect']"
#                 )
#             )
#         )

#     def hover_readiness_bars(self):
#         bars = self.get_readiness_bars()
#         for bar in bars[:5]:
#             ActionChains(self.driver).move_to_element(bar).pause(1).perform()

import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class FacilityStatusPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    # =========================================================
    # STRATEGIC OVERVIEW
    # =========================================================
    def verify_strategic_overview_loaded(self):
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//*[name()='svg']//*[name()='path' and contains(@class,'highcharts-point')]"
                )
            )
        )
        return True

    # =========================================================
    # MAP SECTION
    # =========================================================
    def scroll_to_map_section(self):
        header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Status of All Facilities')]")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", header
        )
        time.sleep(2)

    # def verify_map_visible(self):
    #     self.wait.until(
    #         lambda d: len(
    #             d.find_elements(
    #                 By.XPATH,
    #                 "//*[name()='svg']//*[name()='path' and contains(@class,'highcharts-point')]"
    #             )
    #         ) > 0
    #     )
    #     return True

    def verify_map_visible(self):
        points = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//*[contains(@class,'highcharts-point')]")
            )
        )
        return len(points) > 0

    # def get_facility_map_points(self):
    #     return self.driver.find_elements(
    #         By.XPATH,
    #         "//*[name()='svg']//*[name()='path' and contains(@class,'highcharts-point')]"
    #     )
    def get_facility_map_points(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//*[contains(@class,'highcharts-point')]")
            )
        )

    # def hover_on_map_point(self, point):
    #     self.driver.execute_script(
    #         "arguments[0].scrollIntoView({block:'center'});", point
    #     )
    #     ActionChains(self.driver).move_to_element(point).pause(0.6).perform()
    def hover_on_map_point(self, point):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", point
        )
        ActionChains(self.driver).move_to_element(point).pause(1).perform()

    def hover_multiple_map_circles(self, count=5):
        points = self.get_facility_map_points()
        assert len(points) > 0, "❌ No map points found"

        for p in points[:count]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", p
            )
            ActionChains(self.driver).move_to_element(p).pause(1).perform()

        return True

    # =========================================================
    # KPI CARDS
    # =========================================================
    def get_all_kpi_values(self):
        """
        Reads KPI CARD values from Strategic Overview
        Example values: 80.10%, 12.40%, 7.50%
        """

        # Wait until KPI cards are visible
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'relative') and contains(@class,'justify-center')]//*[contains(text(),'%')]"
                )
            )
        )

        elements = self.driver.find_elements(
            By.XPATH,
            "//div[contains(@class,'relative') and contains(@class,'justify-center')]//*[contains(text(),'%')]"
        )

        values = []

        for el in elements:
            text = el.text.strip()
            if "%" in text:
                try:
                    values.append(float(text.replace("%", "")))
                except ValueError:
                    pass

        return values

    # =========================================================
    # KPI TABLE
    # =========================================================
    def scroll_to_kpi_table(self):
        table = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[normalize-space()='Facility KPIs']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", table
        )
        time.sleep(2)

    def get_all_kpi_facilities(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody//tr"))
        )
        return rows

    def hover_on_kpi_row(self, row):
        ActionChains(self.driver).move_to_element(row).pause(0.5).perform()

    def switch_kpi_view(self, value):
        dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[normalize-space()='Facility KPIs']/following::select[1]")
            )
        )
        Select(dropdown).select_by_visible_text(value)
        time.sleep(2)

    # =========================================================
    # KPI BAR CHART
    # =========================================================
    def get_kpi_bars(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//h2[normalize-space()='Facility KPIs']"
                    "/ancestor::div//*[name()='path' and contains(@class,'highcharts-point')]"
                )
            )
        )

    def hover_on_kpi_bar(self, bar):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", bar
        )
        ActionChains(self.driver).move_to_element(bar).pause(0.6).perform()
