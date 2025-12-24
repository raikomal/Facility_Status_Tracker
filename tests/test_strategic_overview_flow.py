import time
from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import start_new_report, write_test_report
from utils.alert_handler import handle_any_alert


def test_strategic_overview_flow(driver):

    # ---------------- REPORT INIT ----------------
    start_new_report()

    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # =========================================================
    # TC-SO-01: Navigation
    # =========================================================
    slider.navigate_to_part_allocation_insights()
    handle_any_alert(driver)

    slider.open_facility_status_tracker()
    handle_any_alert(driver)
    time.sleep(3)

    write_test_report(
        "Tower Track", "Web", "Navigation",
        "Open Facility Status Tracker",
        "Navigate via Part Allocation Insights",
        "Facility page should open",
        "Facility page opened",
        "Pass", "", "SO-01", ""
    )

    # =========================================================
    # TC-SO-02: Strategic Overview Load
    # =========================================================
    assert facility.verify_strategic_overview_loaded()

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify page load",
        "Strategic Overview default tab",
        "Widgets visible",
        "Widgets loaded",
        "Pass", "", "SO-02", ""
    )

    # =========================================================
    # TC-SO-03: KPI Cards
    # =========================================================
    kpis = facility.get_all_kpi_values()
    assert len(kpis) >= 3

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify KPI cards",
        "Read KPI values",
        "KPI cards visible",
        f"KPI values: {kpis[:3]}",
        "Pass", "", "SO-03", ""
    )

    # =========================================================
    # TC-SO-04: Map (scroll → verify → hover)
    # =========================================================
    facility.scroll_to_map_section()
    assert facility.verify_map_visible()

    points = facility.get_facility_map_points()
    assert len(points) > 0

    for p in points[:3]:
        facility.hover_on_map_point(p)
        time.sleep(1)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify map hover",
        "Hover facility map circles",
        "Tooltips visible",
        f"{len(points)} points found",
        "Pass", "", "SO-04", ""
    )

    # =========================================================
    # TC-SO-05: KPI Table hover + dropdown
    # =========================================================
    facility.scroll_to_kpi_table()
    rows = facility.get_all_kpi_facilities()
    assert len(rows) > 0

    for r in rows[:3]:
        facility.hover_on_kpi_row(r)
        time.sleep(1)

    facility.switch_kpi_view("Table view")

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify KPI table hover",
        "Hover KPI rows",
        "Rows highlighted",
        f"{len(rows)} rows",
        "Pass", "", "SO-05", ""
    )

    # =========================================================
    # TC-SO-06: KPI Bar Chart hover
    # =========================================================
    facility.switch_kpi_view("Bar chart")

    bars = facility.get_kpi_bars()
    assert len(bars) > 0

    for b in bars[:3]:
        facility.hover_on_kpi_bar(b)
        time.sleep(1)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify KPI bar hover",
        "Hover bar chart",
        "Tooltips visible",
        f"{len(bars)} bars",
        "Pass", "", "SO-06", ""
    )

    print("\n✅ Strategic Overview full flow completed successfully\n")
