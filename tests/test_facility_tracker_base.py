import time
from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from tests.login_helper import login_and_reach_dashboard
from utils.csv_writer import start_new_report, write_test_report


def test_facility_tracker_base_navigation(driver):
    """
    Base test:
    - Login (reuse existing logic)
    - Navigate to Facility Status Tracker
    - Verify Strategic Overview loads
    - Create CSV report entries
    """

    # ---------------- REPORT INIT ----------------
    start_new_report()

    # ---------------- LOGIN ----------------
    # (Handled by conftest + login_helper)
    write_test_report(
        "Tower Track",
        "Web",
        "Login",
        "Login to Tower Track",
        "Login with valid credentials",
        "Dashboard should load successfully",
        "Dashboard loaded successfully",
        "Pass",
        "Login reused from existing helper",
        "FST-BASE-01",
        ""
    )

    # ---------------- NAVIGATION ----------------
    # ---------------- NAVIGATION ----------------
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # Step 1: Navigate slider sequentially
    slider.navigate_to_part_allocation_insights()

    write_test_report(
        "Tower Track",
        "Web",
        "Navigation",
        "Navigate to Part Allocation Insights",
        "Click Demand → Capacity → Supply → Part Allocation",
        "Part Allocation Insights should open",
        "Part Allocation Insights opened",
        "Pass",
        "",
        "FST-BASE-02",
        ""
    )

    # Step 2: Open Facility Status Tracker
    slider.hover_and_click_facility_status_tracker()
    time.sleep(4)

    write_test_report(
        "Tower Track",
        "Web",
        "Navigation",
        "Open Facility Status Tracker",
        "Hover and click Facility Status Tracker",
        "Facility Status Tracker page should open",
        "Facility Status Tracker page opened",
        "Pass",
        "",
        "FST-BASE-03",
        ""
    )

    # ---------------- VERIFICATION ----------------
    assert facility.verify_strategic_overview_loaded()

    write_test_report(
        "Tower Track",
        "Web",
        "Facility Tracker",
        "Verify Strategic Overview Load",
        "Check Strategic Overview elements",
        "Strategic Overview should be visible",
        "Strategic Overview loaded successfully",
        "Pass",
        "",
        "FST-BASE-04",
        ""
    )

    print("\n✅ Facility Tracker base navigation completed successfully\n")
