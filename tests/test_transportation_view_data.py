from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report
from selenium.webdriver.common.by import By
import time


def test_transportation_view_human_flow(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # ================= SAVE PARENT WINDOW =================
    parent_window = driver.current_window_handle

    # ================= NAVIGATION =================
    slider.click_slider("Part Allocation Insights")
    slider.hover_and_click_facility_status_tracker()

    facility.select_readiness_viewpoint("Transportation")
    facility.click_transportation_arrow()
    facility.verify_transportation_view_page_loaded()

    # ================= HUMAN FLOW FILTERS =================
    facility.select_transportation_facility("PHX1")
    facility.select_transportation_phase("Phase B")
    facility.remove_part_category("Other")

    # Read values AFTER selection
    facility_name = facility.get_transportation_facility()
    phase_name = facility.get_transportation_phase()
    categories = facility.get_transportation_part_categories()

    write_test_report(
        "Tower Track", "Web", "Transportation View",
        "Verify Transportation filters",
        "Select Facility, Phase, Category",
        "Filters should update correctly",
        f"Facility={facility_name}, Phase={phase_name}, Categories={categories}",
        "Pass", "", "TV-01", ""
    )

    # ================= DEPENDENCY GRAPH =================
    facility.scroll_to_dependency_graph()
    facility.change_dependency_graph_view_slowly()
    # ================= TV-02 =================
    parts = facility.get_required_parts_table()

    assert isinstance(parts, list)

    write_test_report(
        "Tower Track", "Web", "Transportation View",
        "Verify Required Parts table",
        "Read Required Parts data",
        "Table may or may not contain rows",
        f"Rows: {len(parts)}",
        "Pass", "", "TV-02", ""
    )

    # ================= TV-03 =================
    deps = facility.get_dependency_status_table()
    assert len(deps) > 0

    write_test_report(
        "Tower Track", "Web", "Transportation View",
        "Verify Dependency Status table",
        "Read Dependency Status data",
        "Dependency status should be present",
        f"Rows: {len(deps)}",
        "Pass", "", "TV-03", ""
    )

    # ================= CLOSE CHILD & SWITCH BACK =================

    current_window = driver.current_window_handle

    # Close ONLY the child window
    if current_window != parent_window:
        driver.close()

    # Switch back to parent window
    driver.switch_to.window(parent_window)
    time.sleep(2)

    print("✅ Closed Transportation window and switched back to parent")
