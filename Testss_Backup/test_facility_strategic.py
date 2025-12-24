from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from tests.login_helper import login_and_reach_dashboard
from utils.csv_writer import write_test_report, start_new_report
import time


def test_strategic_overview_map_hover_multiple(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    try:
        slider = SliderPage(driver)
        facility = FacilityStatusPage(driver)

        # 🔒 EXISTING WORKING FLOW (DO NOT MODIFY)
        slider.click_slider("Part Allocation Insights")
        time.sleep(2)

        slider.hover_and_click_facility_status_tracker()
        time.sleep(3)

        # 🟢 STRATEGIC OVERVIEW
        facility.click_strategic_overview()
        facility.verify_strategic_overview_loaded()

        # 🗺 MAP POINTS
        points = facility.get_facility_points()
        max_points = min(6, len(points))

        for i in range(max_points):
            # 🔁 IMPORTANT: re-fetch elements every time
            points = facility.get_facility_points()
            facility.hover_on_specific_facility(points[i])
            time.sleep(1.5)

            assert facility.is_tooltip_visible()

            write_test_report(
                "Tower Track",
                "Web",
                "Strategic Overview",
                f"Hover on map circle {i + 1}",
                f"Hover on facility circle {i + 1}",
                "Tooltip should appear",
                "Tooltip appeared",
                "Pass",
                "",
                f"MAP-HOVER-0{i + 1}",
                ""
            )

    finally:
        driver.quit()
