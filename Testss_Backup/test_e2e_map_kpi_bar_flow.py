import time
from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage


def test_full_strategic_overview_page(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    print("\n========== STRATEGIC OVERVIEW FULL PAGE TEST ==========\n")

    # ---------------- NAVIGATION ----------------
    slider.click_slider("Part Allocation Insights")
    facility.demo_pause(2)

    slider.hover_and_click_facility_status_tracker()
    facility.demo_pause(2)

    facility.click_strategic_overview()
    assert facility.verify_strategic_overview_loaded()
    facility.demo_pause(2)

    # ---------------- MAP ----------------
    print("🔵 Map hover")
    points = facility.get_facility_map_points()
    for p in points[:3]:
        facility.hover_on_map_point(p)
        facility.demo_pause(1)

    # ---------------- KPI TABLE ----------------
    print("📊 KPI table")
    facility.scroll_to_kpi_table()
    facility.demo_pause(2)

    facility.scroll_kpi_table_fully()
    facilities = facility.get_all_kpi_facilities()

    for f in facilities[:3]:
        facility.hover_on_kpi_row(f)
        facility.demo_pause(1)

    # ---------------- KPI BAR CHART ----------------
    print("📈 KPI bar chart")
    facility.switch_kpi_view("barchart")
    bars = facility.get_kpi_bars()

    for bar in bars[:3]:
        facility.hover_on_kpi_bar(bar)
        facility.demo_pause(1)

 
    # ---------------- READINESS SUMMARY ----------------
    print("📉 Facility Readiness Summary")
    facility.select_readiness_view("Facility ViewPoint")
    facility.hover_readiness_bars()

    print("\n✅ FULL STRATEGIC OVERVIEW PAGE TEST COMPLETED\n")
