from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import start_new_report, write_test_report
import time


def test_facility_kpis(driver):
   

    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # ===============================
    # NAVIGATION
    # ===============================
    slider.click_slider("Part Allocation Insights")
    time.sleep(3)

    slider.hover_and_click_facility_status_tracker()
    time.sleep(5)  # heavy dashboard load

    # ===============================
    # SCROLL FLOW (IMPORTANT)
    # ===============================
    facility.scroll_to_bottom()   # load all widgets
    facility.scroll_to_top()      # return to KPI section

    # ===============================
    # KPI VALIDATIONS
    # ===============================
    assert facility.wait_for_kpis_to_load()

    kpi_values = facility.get_all_kpi_values()

    print("📊 KPI VALUES FOUND:", kpi_values)

    # Validation 1: At least 3 KPIs
    assert len(kpi_values) >= 3, "Less than 3 KPI values found"

    # Validation 2: KPI range check
    for value in kpi_values[:3]:
        assert 0 <= value <= 100, f"Invalid KPI value: {value}"

    write_test_report(
        "Tower Track",
        "Web",
        "Facility KPIs",
        "Verify Facility KPI cards",
        "Scroll page, load KPIs, validate values",
        "All KPI values should be visible and valid",
        f"KPI Values: {kpi_values[:3]}",
        "Pass",
        "",
        "FAC-KPI-01",
        ""
    )
