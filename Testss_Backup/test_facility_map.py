from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from tests.login_helper import login_and_reach_dashboard
import time


def test_strategic_overview_map_basic(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)


    try:
        slider = SliderPage(driver)

        facility = FacilityStatusPage(driver)

        # Stable, existing navigation
        slider.click_slider("Part Allocation Insights")
        time.sleep(2)

        slider.hover_and_click_facility_status_tracker()
        time.sleep(3)

        # 🟢 INSIDE PAGE TESTING STARTS
        assert facility.verify_map_visible()

        points = facility.get_facility_points()
        points_count = len(points)

        print(f"🗺 Map points found: {points_count}")

        assert points_count > 0, "No facility points found on map"

    finally:
        driver.quit()
