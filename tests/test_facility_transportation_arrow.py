import time
from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report


def test_facility_transportation_arrow(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    slider.click_slider("Part Allocation Insights")
    slider.hover_and_click_facility_status_tracker()

    # ================= SO-16 =================
    facility.select_readiness_viewpoint("Transportation")

    facility.click_transportation_arrow()

    facility.verify_transportation_view_page_loaded()

    write_test_report(
        "Tower Track", "Web", "Transportation View",
        "Verify Transportation Dependency Readiness navigation",
        "Select Transportation viewpoint and click arrow",
        "Transportation View page should open",
        "Transportation Dependency Readiness page opened successfully",
        "Pass", "", "SO-16", ""
    )
