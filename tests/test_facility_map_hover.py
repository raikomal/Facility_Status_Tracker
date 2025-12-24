# from pages.slider_page import SliderPage
# from pages.facility_status_page import FacilityStatusPage
# from tests.login_helper import login_and_reach_dashboard
# from utils.csv_writer import start_new_report, write_test_report
# import time
#
#
# def test_strategic_overview_map_hover_multiple(driver):
#     slider = SliderPage(driver)
#     facility = FacilityStatusPage(driver)
#
#     try:
#         slider = SliderPage(driver)
#         facility = FacilityStatusPage(driver)
#
#         slider.click_slider("Part Allocation Insights")
#         write_test_report(
#             "Tower Track", "Web", "Dashboard",
#             "Open Part Allocation Insights",
#             "Click Part Allocation Insights slider",
#             "Slider should open",
#             "Slider opened",
#             "Pass", "", "DASH-01", ""
#         )
#
#         time.sleep(2)
#
#         slider.hover_and_click_facility_status_tracker()
#         write_test_report(
#             "Tower Track", "Web", "Facility",
#             "Open Facility Status Tracker",
#             "Hover and click Facility Status Tracker card",
#             "Facility page should open",
#             "Facility page opened",
#             "Pass", "", "FAC-01", ""
#         )
#
#         time.sleep(3)
#
#         facility.verify_strategic_overview_loaded()
#         write_test_report(
#             "Tower Track", "Web", "Strategic Overview",
#             "Verify Strategic Overview",
#             "Check Strategic Overview page",
#             "Strategic Overview should load",
#             "Strategic Overview loaded",
#             "Pass", "", "SO-01", ""
#         )
#
#         points = facility.get_facility_points()
#
#         max_points = min(6, len(points))
#
#         max_points = min(6, len(points))
#
#         for i in range(max_points):
#             facility.hover_on_specific_facility(points[i])
#             time.sleep(1.5)
#
#             write_test_report(
#                 "Tower Track", "Web", "Strategic Overview",
#                 f"Hover on map circle {i + 1}",
#                 f"Hover on facility circle {i + 1}",
#                 "Tooltip should appear",
#                 "Tooltip appeared",
#                 "Pass", "", f"MAP-HOVER-0{i + 1}", ""
#             )
#
#
#     finally:
#         driver.quit()

from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import start_new_report, write_test_report
import time


def test_strategic_overview_map_hover_multiple(driver):
    start_new_report()

    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # ===============================
    # SESSION-SAFE NAVIGATION
    # ===============================
    if "Part Allocation Insights" not in driver.page_source:
        slider.click_slider("Part Allocation Insights")
        write_test_report(
            "Tower Track", "Web", "Dashboard",
            "Open Part Allocation Insights",
            "Click Part Allocation Insights slider",
            "Slider should open",
            "Slider opened",
            "Pass", "", "DASH-01", ""
        )
        time.sleep(2)

    slider.hover_and_click_facility_status_tracker()
    write_test_report(
        "Tower Track", "Web", "Facility",
        "Open Facility Status Tracker",
        "Hover and click Facility Status Tracker card",
        "Facility page should open",
        "Facility page opened",
        "Pass", "", "FAC-01", ""
    )
    time.sleep(3)

    # ===============================
    # PAGE VERIFICATION
    # ===============================
    facility.verify_strategic_overview_loaded()
    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify Strategic Overview",
        "Check Strategic Overview page",
        "Strategic Overview should load",
        "Strategic Overview loaded",
        "Pass", "", "SO-01", ""
    )

    # ===============================
    # MAP HOVER VALIDATION
    # ===============================
    points = facility.get_facility_map_points()
    max_points = min(6, len(points))

    for i in range(max_points):
        facility.hover_on_specific_facility(points[i])
        time.sleep(1.5)

        write_test_report(
            "Tower Track", "Web", "Strategic Overview",
            f"Hover on map circle {i + 1}",
            f"Hover on facility circle {i + 1}",
            "Tooltip should appear",
            "Tooltip appeared",
            "Pass", "", f"MAP-HOVER-0{i + 1}", ""
        )

