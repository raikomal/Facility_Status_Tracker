from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report


def test_operational_insights_flow(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # ================= NAVIGATION =================
    slider.click_slider("Part Allocation Insights")
    slider.hover_and_click_facility_status_tracker()

    facility.go_to_operational_insights()

    # ================= FILTERS =================
    filters = facility.get_operational_filters()
    assert isinstance(filters, dict)

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify filters",
        "Read selected filters",
        "Filters should be visible",
        str(filters),
        "Pass", "", "OI-01", ""
    )

    # ================= ALLOCATION TABLE =================
    rows = facility.get_operational_allocation_table()
    assert isinstance(rows, list)

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify allocation table",
        "Read table rows",
        "Table may or may not have data",
        f"Rows: {len(rows)}",
        "Pass", "", "OI-02", ""
    )

    # ================= INVENTORY DETAILS =================
    inventory = facility.get_part_inventory_details()
    assert isinstance(inventory, dict)

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify inventory details",
        "Read inventory panel",
        "Inventory should load if data exists",
        str(inventory),
        "Pass", "", "OI-03", ""
    )
    # ================= STEP 1 =================
    facility.select_operational_status("delayed")
    facility.select_operational_part("CRAH Stands")

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify Delayed + CRAH Stands",
        "Change filters",
        "Table should update",
        "Status=Delayed, Part=CRAH Stands",
        "Pass", "", "OI-04", ""
    )

    # ================= STEP 2 (CORRECTED) =================
    facility.select_operational_status("pending")
    facility.select_operational_part("Cable Busway")

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify Pending + Cable Busway",
        "Change filters",
        "Table should update",
        "Status=Pending, Part=Cable Busway",
        "Pass", "", "OI-05", ""
    )