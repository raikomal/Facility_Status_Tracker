# from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report
import time


def test_strategic_overview_facility_kpis(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    try:
        # -----------------------------
        # Navigation
        # -----------------------------
        slider.click_slider("Part Allocation Insights")
        time.sleep(2)

        slider.hover_and_click_facility_status_tracker()
        time.sleep(3)

        # -----------------------------
        # Strategic Overview
        # -----------------------------
        facility.click_strategic_overview()
        assert facility.verify_strategic_overview_loaded()

        # -----------------------------
        # KPI Table Validation
        # -----------------------------
        facility.scroll_to_kpi_table()
        time.sleep(1)

        assert facility.verify_kpi_headers()
        assert facility.verify_facility_row_present("PHX1")

        # -----------------------------
        # CSV REPORT (PASS)
        # -----------------------------
        write_test_report(
            "Tower Track",
            "Web",
            "Strategic Overview",
            "Facility KPI table validation",
            "Scroll to KPI table and verify headers & facility row",
            "KPI headers and facility data should be visible",
            "KPI headers and facility data verified successfully",
            "Pass",
            "",
            "KPI-TABLE-01",
            ""
        )

        print("✅ Strategic Overview – Facility KPIs verified with scroll")

    except Exception as e:
        # -----------------------------
        # CSV REPORT (FAIL)
        # -----------------------------
        write_test_report(
            "Tower Track",
            "Web",
            "Strategic Overview",
            "Facility KPI table validation",
            "Scroll to KPI table and verify headers & facility row",
            "KPI headers and facility data should be visible",
            f"Failure: {str(e)}",
            "Fail",
            "",
            "KPI-TABLE-01",
            ""
        )
        raise
