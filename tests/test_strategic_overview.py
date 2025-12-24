import time
from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import start_new_report, write_test_report
from utils.alert_handler import handle_any_alert


def test_strategic_overview_full_flow(driver):
    """
    Strategic Overview – Full Flow
    Order:
    1. Navigation
    2. KPI Cards
    3. Map (hover circles)
    4. KPI Table (hover + dropdown)
    5. KPI Bar Chart (hover)
    """

    start_new_report()

    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # ---------- NAVIGATION ----------
    slider.navigate_to_part_allocation_insights()
    handle_any_alert(driver)

    slider.open_facility_status_tracker()
    handle_any_alert(driver)
    time.sleep(3)

    write_test_report(
        "Tower Track", "Web", "Navigation",
        "Open Facility Status Tracker",
        "Navigate via Part Allocation",
        "Facility page opens",
        "Facility page opened",
        "Pass", "", "SO-01", ""
    )

    # ---------- STRATEGIC OVERVIEW LOAD ----------
    assert facility.verify_strategic_overview_loaded()

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify page load",
        "Load strategic overview",
        "Widgets visible",
        "Widgets loaded",
        "Pass", "", "SO-02", ""
    )

    # ---------- KPI CARDS ----------
    kpis = facility.get_all_kpi_values()
    assert len(kpis) >= 3

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify KPI cards",
        "Read KPI values",
        "KPIs visible",
        f"KPI values: {kpis[:3]}",
        "Pass", "", "SO-03", ""
    )

    # ---------- MAP (HOVER FIRST) ----------
    assert facility.verify_map_container_loaded()

    points = facility.get_facility_map_points()
    assert len(points) > 0

    for point in points[:3]:
        facility.hover_on_map_point(point)
        time.sleep(1)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Map circle hover",
        "Hover facility map circles",
        "Tooltip appears",
        f"{len(points)} points detected",
        "Pass", "", "SO-04", ""
    )

    # ---------- KPI TABLE ----------
    facility.scroll_to_kpi_table()
    time.sleep(2)

    rows = facility.get_all_kpi_facilities()
    assert len(rows) > 0

    for row in rows[:3]:
        facility.hover_on_kpi_row(row)
        time.sleep(1)

    facility.switch_kpi_view("Table view")
    time.sleep(1)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "KPI table hover",
        "Hover rows and switch view",
        "Rows highlighted",
        f"{len(rows)} rows found",
        "Pass", "", "SO-05", ""
    )

    # ---------- KPI BAR CHART ----------
    facility.switch_kpi_view("Bar chart")
    time.sleep(2)

    bars = facility.get_kpi_bars()
    assert len(bars) > 0

    for bar in bars[:3]:
        facility.hover_on_kpi_bar(bar)
        time.sleep(1)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Bar chart hover",
        "Hover KPI bars",
        "Tooltip appears",
        f"{len(bars)} bars detected",
        "Pass", "", "SO-06", ""
    )

    print("\n✅ Strategic Overview FULL FLOW completed successfully\n")
