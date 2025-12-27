from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report
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

    # ================= FILTERS =================
    facility.select_transportation_facility("PHX1")
    facility.select_transportation_phase("Phase B")
    facility.remove_part_category("Other")

    # ================= DEPENDENCY GRAPH =================
    facility.scroll_to_dependency_graph()
    facility.change_dependency_graph_view_slowly()

    # ================= REQUIRED PARTS =================
    parts = facility.get_required_parts_table()

    # ✅ THIS IS WHERE assert isinstance(parts, list) GOES
    assert isinstance(parts, list)

    write_test_report(
        "Tower Track", "Web", "Transportation View",
        "Verify Required Parts",
        "Read table",
        "Table may or may not contain rows",
        f"Rows: {len(parts)}",
        "Pass", "", "TV-02", ""
    )

    # ================= DEPENDENCY STATUS =================
    deps = facility.get_dependency_status_table()

    assert isinstance(deps, list)

    write_test_report(
        "Tower Track", "Web", "Transportation View",
        "Verify Dependency Status",
        "Read table",
        "Table may or may not contain rows",
        f"Rows: {len(deps)}",
        "Pass", "", "TV-03", ""
    )

    # ================= CLOSE CHILD & SWITCH BACK =================
    if driver.current_window_handle != parent_window:
        driver.close()

    driver.switch_to.window(parent_window)
    time.sleep(2)

    print("✅ Transportation tab closed and returned to parent")
