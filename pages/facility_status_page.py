from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time




class FacilityStatusPage:
    """
    Page Object: Facility Status Tracker – Strategic Overview
    Highcharts-safe implementation (NO infinite waits)
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    # =========================================================
    # ONE-TIME PAGE READY (MAP SVG LOAD)
    # =========================================================
    def wait_for_map_svg_once(self):
        """
        Wait ONLY ONCE for Highcharts map bubbles to exist.
        Call immediately after navigation.
        """
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 "g.highcharts-mapbubble-series path.highcharts-point")
            )
        )
        return True

    # =========================================================
    # SCROLL HELPERS
    # =========================================================
    def scroll_to_map_section(self):
        header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//h2[normalize-space()='Status of All Facilities']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            header
        )
        time.sleep(0.3)

    def scroll_to_kpi_table(self):
        header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//h2[normalize-space()='Facility KPIs']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            header
        )
        time.sleep(0.3)

    # =========================================================
    # KPI CARDS (TOP SUMMARY)
    # =========================================================
    def get_kpi_card_values(self):
        """
        Reads KPI cards at top (80.10%, 12.40%, 7.50%)
        """
        cards = self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'rounded-lg')]"
                    "//div[contains(text(),'%')]"
                )
            )
        )

        values = []
        for card in cards:
            txt = card.text.strip()
            if "%" in txt:
                try:
                    values.append(float(txt.replace("%", "")))
                except ValueError:
                    pass

        return values

    # =========================================================
    # MAP → FULFILLMENT RATE
    # =========================================================
    def get_facility_map_points(self):
        """
        Returns map bubbles ONLY.
        """
        self.scroll_to_map_section()

        return self.driver.find_elements(
            By.CSS_SELECTOR,
            "g.highcharts-mapbubble-series path.highcharts-point"
        )

    def hover_multiple_map_circles(self, count=5):
        points = self.get_facility_map_points()
        assert len(points) > 0, "No map points found"

        for point in points[:count]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                point
            )
            ActionChains(self.driver)\
                .move_to_element(point)\
                .pause(0.4)\
                .perform()

        return True

    # =========================================================
    # KPI TABLE → MISALLOCATION RATE
    # =========================================================
    def wait_for_kpis_to_load(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr"))
        )
        return True

    def get_all_kpi_facilities(self):
        rows = self.driver.find_elements(By.XPATH, "//tbody/tr")

        facilities = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if cols:
                facilities.append(cols[0].text.strip())

        return facilities

    def get_misallocation_rate_values(self):
        rows = self.driver.find_elements(By.XPATH, "//tbody/tr")

        values = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 3:
                txt = cols[2].text.strip()
                if "%" in txt:
                    try:
                        values.append(float(txt.replace("%", "")))
                    except ValueError:
                        pass

        return values

    def hover_on_kpi_row(self, facility_name):
        cell = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//td[normalize-space()='{facility_name}']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            cell
        )
        ActionChains(self.driver)\
            .move_to_element(cell)\
            .pause(0.4)\
            .perform()

    # =========================================================
    # KPI VIEW SWITCH
    # =========================================================
    def switch_kpi_view(self, view="table"):
        """
        view = 'table' or 'barchart'
        """
        dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//h2[normalize-space()='Facility KPIs']/following::select[1]")
            )
        )
        Select(dropdown).select_by_value(view)
        time.sleep(0.8)

    # =========================================================
    # BAR CHART → REALLOCATION RATE
    # =========================================================
    def get_bar_chart_columns(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 "g.highcharts-series.highcharts-column-series")
            )
        )

        return self.driver.find_elements(
            By.CSS_SELECTOR,
            "g.highcharts-series.highcharts-column-series "
            "path.highcharts-point"
        )

    def hover_on_bar(self, bar):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            bar
        )

        ActionChains(self.driver)\
            .move_to_element(bar)\
            .pause(0.3)\
            .move_by_offset(10, -10)\
            .pause(0.5)\
            .perform()

    # =========================================================
    # =========================================================
    # SANKEY CHART (SAFE VERSION)
    # =========================================================
    def hover_flow_links(self, count=5):
        """
        Hover over Sankey flow links (Highcharts path elements)
        """
        links = self.get_flow_links()
        count = min(count, len(links))

        for link in links[:count]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", link
            )
            ActionChains(self.driver) \
                .move_to_element(link) \
                .pause(0.5) \
                .perform()

        return True

    def verify_sankey_chart_visible(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[name()='path' and contains(@class,'highcharts-link')]")
            )
        )
        return True

    def get_flow_links(self):
        return self.driver.find_elements(
            By.XPATH,
            "//*[name()='path' and contains(@class,'highcharts-link')]"
        )

    def hover_single_flow_link(self):
        links = self.get_flow_links()
        assert links, "No Sankey links found"

        link = links[0]
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", link
        )
        ActionChains(self.driver).move_to_element(link).pause(0.6).perform()

    def get_sankey_tooltip_text(self):
        tooltips = self.driver.find_elements(
            By.XPATH,
            "//*[name()='g' and contains(@class,'highcharts-tooltip')]//*[name()='text']"
        )
        return " ".join(t.text.strip() for t in tooltips if t.text.strip())

    def validate_sankey_tooltip_structure(self, tooltip_text: str):
        """
        Valid Sankey tooltip can be:
        - Node tooltip (label only)
        - OR Link tooltip (source → target with value)
        """
        if not tooltip_text:
            return False

        has_text = any(char.isalpha() for char in tooltip_text)
        has_number = any(char.isdigit() for char in tooltip_text)
        has_arrow = "→" in tooltip_text or "to" in tooltip_text.lower()

        # Accept node OR link tooltip
        return has_text and (has_number or has_arrow)

    def hover_multiple_sankey_links(self, count=5):
        links = self.get_flow_links()
        hovered = 0

        for link in links[:count]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", link
            )
            ActionChains(self.driver).move_to_element(link).pause(0.4).perform()
            hovered += 1

        return hovered

    def sankey_tooltip_has_non_zero_value(self, tooltip_text):
        numbers = []
        for part in tooltip_text.replace(",", "").split():
            try:
                numbers.append(float(part))
            except ValueError:
                pass
        return any(n > 0 for n in numbers)

    # =========================================================
    # SANKEY DROPDOWN (Distributor → Facility Flow)
    # =========================================================
    def get_sankey_dropdown(self):
        """
        Returns Sankey chart dropdown (Distributor selector)
        """
        return self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='flex items-center gap-2 mr-2']//select"
                )
            )
        )

    # def scroll_to_readiness_summary(self):
    #     header = self.wait.until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, "//h2[normalize-space()='Facility Status Readiness Summary']")
    #         )
    #     )
    #     self.driver.execute_script(
    #         "arguments[0].scrollIntoView({block:'center'});", header
    #     )
    #     time.sleep(1)

    # def get_readiness_viewpoint_dropdown(self):
    #     """
    #     Facility / Resource / Transportation / Alert dropdown
    #     """
    #     return self.wait.until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, "//select[contains(@class,'rounded-md') and contains(@class,'text-black')]")
    #         )
    #     )
    #
    # def select_readiness_viewpoint(self, view):
    #     """
    #     view: Facility | Resource | Transportation | Alert
    #     UI text: Facility ViewPoint | Resource ViewPoint | ...
    #     """
    #
    #     dropdown = self.wait.until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, "//select[contains(@class,'rounded-md')]")
    #         )
    #     )
    #
    #     # Map simple names to actual dropdown text
    #     view_map = {
    #         "Facility": "Facility ViewPoint",
    #         "Resource": "Resource ViewPoint",
    #         "Transportation": "Transportation ViewPoint",
    #         "Alert": "Alert ViewPoint",
    #     }
    #
    #     visible_text = view_map.get(view)
    #     assert visible_text, f"Invalid readiness view: {view}"
    #
    #     Select(dropdown).select_by_visible_text(visible_text)
    #
    #     # Allow Highcharts redraw
    #     time.sleep(2)
    #
    # def get_readiness_chart_container(self):
    #     """
    #     Returns ONLY the Facility Status Readiness Summary chart container
    #     """
    #     return self.wait.until(
    #         EC.presence_of_element_located(
    #             (
    #                 By.XPATH,
    #                 "//h2[contains(text(),'Facility Status Readiness Summary')]"
    #                 "/following::div[contains(@class,'highcharts-container')][1]"
    #             )
    #         )
    #     )
    #
    # def get_readiness_bars(self):
    #     """
    #     ONLY readiness bars (uses aria-label like:
    #     'NYC2, 61, Readiness Score')
    #     """
    #     container = self.get_readiness_chart_container()
    #
    #     return self.wait.until(
    #         EC.presence_of_all_elements_located(
    #             (
    #                 By.XPATH,
    #                 ".//*[name()='path' and contains(@class,'highcharts-point') "
    #                 "and contains(@aria-label,'Readiness')]"
    #             )
    #         )
    #     )
    #
    # def wait_for_readiness_bars(self):
    #     """
    #     Wait ONLY for Facility Status Readiness bars
    #     Uses aria-label to avoid map / sankey / KPI confusion
    #     """
    #     return self.wait.until(
    #         EC.presence_of_all_elements_located(
    #             (
    #                 By.XPATH,
    #                 "//*[name()='path' "
    #                 "and contains(@class,'highcharts-point') "
    #                 "and contains(@aria-label,'Readiness')]"
    #             )
    #         )
    #     )
    #
    # def hover_readiness_bars(self, view="Facility"):
    #     # Transportation has no bars
    #     if view == "Transportation":
    #         return True
    #
    #     container = self.get_readiness_chart_container()
    #     self.driver.execute_script(
    #         "arguments[0].scrollIntoView({block:'center'});", container
    #     )
    #     time.sleep(1)
    #
    #     bars = self.get_readiness_bars()
    #     assert len(bars) > 0, "No readiness bars found"
    #
    #     # Hover only first 2–3 bars (safe)
    #     for bar in bars[:3]:
    #         ActionChains(self.driver).move_to_element(bar).pause(0.4).perform()
    #
    #     return True
    #
    # def click_transportation_arrow(self):
    #     arrow = self.wait.until(
    #         EC.element_to_be_clickable(
    #             (
    #                 By.XPATH,
    #                 "//h2[normalize-space()='Transportation Dependency Readiness Summary']"
    #                 "/following::button[1]"
    #             )
    #         )
    #     )
    #
    #     self.driver.execute_script("arguments[0].click();", arrow)
    #     time.sleep(2)
    #
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
    #
    # ================= FACILITY STATUS READINESS SUMMARY =================

    def verify_readiness_chart_visible(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Readiness')]")
            )
        )
        return True

    def select_readiness_viewpoint(self, view):
        value_map = {
            "Facility": "facility",
            "Resource": "resource",
            "Transportation": "transportation",
            "Alert": "alert",
        }

        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//select[contains(@class,'w-56')]")
            )
        )

        Select(dropdown).select_by_value(value_map[view])
        time.sleep(2)

    def get_readiness_bars(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//*[name()='path' and contains(@class,'highcharts-point') "
                    "and contains(@aria-label,'Readiness Score')]"
                )
            )
        )

    def hover_readiness_bars(self):
        """
        Hover ONLY readiness bars (Facility ViewPoint only)
        """

        bars = self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//*[name()='path' and contains(@class,'highcharts-point') "
                    "and contains(@aria-label,'Readiness Score')]"
                )
            )
        )

        assert len(bars) > 0, "No readiness bars found (Facility ViewPoint)"

        for bar in bars[:3]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", bar
            )
            ActionChains(self.driver).move_to_element(bar).pause(0.4).perform()

        return True

    def click_transportation_arrow(self):
        arrow = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(text(),'Transportation Dependency Readiness Summary')]"
                    "/following::button[1]"
                )
            )
        )
        arrow.click()
        time.sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[-1])
