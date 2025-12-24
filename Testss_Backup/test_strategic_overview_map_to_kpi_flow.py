from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report
import time


def test_map_hover_then_kpi_validation(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    try:
        # -----------------------------
        # Navigation
        # -----------------------------
        slider.click_slider("Part Allocation Insights")
        slider.hover_and_click_facility_status_tracker()

        facility.click_strategic_overview()
        assert facility.verify_strategic_overview_loaded()

        # -----------------------------
        # MAP HOVER (USER-LIKE)
        # -----------------------------
        points = facility.get_facility_map_points()
        assert points, "No map points found"

        facility.hover_on_map_point(points[0])
        time.sleep(0.5)

        # -----------------------------
        # KPI TABLE SCROLL & VALIDATION
        # -----------------------------
        facility.scroll_to_kpi_table()
        facility.scroll_kpi_table_fully()

        facilities = facility.get_all_kpi_facilities()
        assert len(facilities) > 0, "No KPI rows loaded"

        random_facility = facility.get_random_kpi_facility()
        print(f"🎯 Random KPI selected: {random_facility}")

        facility.hover_on_kpi_row(random_facility)
        time.sleep(0.5)
        assert facility.is_map_reacting()

        # -----------------------------
        # CSV REPORT (PASS)
        # -----------------------------
        write_test_report(
            "Tower Track",
            "Web",
            "Strategic Overview",
            "Map to KPI to Map interaction flow validation",
            "Hover on map point, scroll KPI table and hover KPI row",
            "Map and KPI should react to each other correctly",
            "Map and KPI interaction flow verified successfully",
            "Pass",
            "",
            "MAP-KPI-01",
            ""
        )

        print("✅ Map → KPI → Map flow verified successfully")

    except Exception as e:
        # -----------------------------
        # CSV REPORT (FAIL)
        # -----------------------------
        write_test_report(
            "Tower Track",
            "Web",
            "Strategic Overview",
            "Map to KPI to Map interaction flow validation",
            "Hover on map point, scroll KPI table and hover KPI row",
            "Map and KPI should react to each other correctly",
            f"Failure: {str(e)}",
            "Fail",
            "",
            "MAP-KPI-01",
            ""
        )
        raise
