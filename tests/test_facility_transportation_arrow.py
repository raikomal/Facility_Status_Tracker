import time
from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report


def test_facility_transportation_arrow(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # ================= NAVIGATION =================
    slider.click_slider("Part Allocation Insights")
    slider.hover_and_click_facility_status_tracker()

    # ================= READINESS → TRANSPORTATION =================
    facility.select_readiness_viewpoint("Transportation")

    # ⏳ Allow React to fully render Transportation section
    time.sleep(1.5)

    # 👀 Scroll to Transportation Readiness section (human-visible)
    facility.verify_readiness_chart_visible()

    # ================= CLICK TRANSPORTATION ARROW =================
    parent_window = driver.current_window_handle

    facility.click_transportation_arrow()

    # ================= VERIFY NEW TAB =================
    facility.verify_transportation_view_page_loaded()

    # ✅ Assert tab switch happened
    assert driver.current_window_handle != parent_window, \
        "Transportation arrow did not open a new tab"

    write_test_report(
        "Tower Track", "Web", "Transportation View",
        "Verify Transportation Dependency Readiness navigation",
        "Select Transportation viewpoint and click arrow",
        "Transportation View page should open in new tab",
        "Transportation Dependency Readiness page opened successfully",
        "Pass", "", "SO-16", ""
    )
