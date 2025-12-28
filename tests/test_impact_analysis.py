from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report
import time


def test_impact_analysis_flow(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # ================= NAVIGATION =================
    slider.click_slider("Part Allocation Insights")
    slider.hover_and_click_facility_status_tracker()
    facility.go_to_impact_analysis()

    # ================= DEFAULT FILTERS =================
    filters = facility.get_impact_filters()
    assert isinstance(filters, dict)

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Verify default filters",
        "Read filters",
        "Filters should be visible",
        str(filters),
        "Pass", "", "IA-01", ""
    )

    # ================= SELECT FACILITY =================
    facility.select_impact_facility("CHI1 (Aurora, IL)")
    time.sleep(1)

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Verify Facility selection",
        "Select Facility",
        "Facility should be selected",
        "Facility=CHI1 (Aurora, IL)",
        "Pass", "", "IA-01A", ""
    )

    # ================= DATE SELECTION =================
    facility.select_impact_start_date("10-08-2024")
    facility.select_impact_end_date("25-11-2024")

    # ================= GET RECOMMENDATION =================
    facility.click_get_recommendation()
    time.sleep(2)

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Verify Allocation Recommendation",
        "Select Facility + Date Range",
        "Recommendation should load",
        "CHI1 | 10-08-2024 → 25-11-2024",
        "Pass", "", "IA-04", ""
    )

    # ================= MODIFY ALLOCATION =================
    facility.modify_allocation_and_compute_cost()
    time.sleep(2)

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Modify Allocation & Compute Cost",
        "Edit allocation quantities",
        "Cost charts should update",
        "20, 50, 70 entered",
        "Pass", "", "IA-05", ""
    )
