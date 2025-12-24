# from pages.slider_page import SliderPage
# from pages.facility_status_page import FacilityStatusPage
# import time


# def test_kpi_to_map_interaction_multiple(driver):
#     slider = SliderPage(driver)
#     facility = FacilityStatusPage(driver)

#     slider.click_slider("Part Allocation Insights")
#     slider.hover_and_click_facility_status_tracker()

#     facility.click_strategic_overview()
#     assert facility.verify_strategic_overview_loaded()

#     facility.scroll_to_kpi_table()

#     facility_names = ["PHX1", "PHX2", "PHX3", "PHX4", "PHX5"]

#     for name in facility_names:
#         facility.hover_on_kpi_row(name)
#         time.sleep(0.5)
#         assert facility.is_map_reacting(), f"Map did not react for KPI {name}"
#         print(f"✅ KPI → Map interaction verified for {name}")

from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report
import time


def test_kpi_to_map_interaction_multiple(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # -----------------------------
    # Navigation
    # -----------------------------
    slider.click_slider("Part Allocation Insights")
    slider.hover_and_click_facility_status_tracker()

    # -----------------------------
    # Strategic Overview
    # -----------------------------
    facility.click_strategic_overview()
    assert facility.verify_strategic_overview_loaded()

    facility.scroll_to_kpi_table()

    facility_names = ["PHX1", "PHX2", "PHX3", "PHX4", "PHX5"]

    for name in facility_names:
        try:
            # Hover on KPI row
            facility.hover_on_kpi_row(name)
            time.sleep(0.5)

            # Verify map reaction
            assert facility.is_map_reacting()

            # -----------------------------
            # CSV REPORT (PASS)
            # -----------------------------
            write_test_report(
                "Tower Track",
                "Web",
                "Strategic Overview",
                "KPI to Map interaction validation",
                "Hover on KPI row",
                "Map should react/highlight related facility",
                "Map reacted successfully",
                "Pass",
                "",
                "KPI-MAP-01",
                ""
            )

            print(f"✅ KPI → Map interaction verified for {name}")

        except Exception as e:
            # -----------------------------
            # CSV REPORT (FAIL)
            # -----------------------------
            write_test_report(
                "Tower Track",
                "Web",
                "Strategic Overview",
                "KPI to Map interaction validation",
                "Hover on KPI row",
                "Map should react/highlight related facility",
                f"Failure: {str(e)}",
                "Fail",
                "",
                "KPI-MAP-01",
                ""
            )
            raise
