from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage


def test_kpi_barchart_dropdown_and_hover(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # -----------------------------
    # Navigation (reuse stable path)
    # -----------------------------
    slider.click_slider("Part Allocation Insights")
    slider.hover_and_click_facility_status_tracker()

    facility.click_strategic_overview()
    assert facility.verify_strategic_overview_loaded()

    # -----------------------------
    # KPI SECTION
    # -----------------------------
    facility.scroll_to_kpi_table()

    # Switch KPI view → Bar chart (SELECT dropdown)
    facility.switch_kpi_view("barchart")

    # -----------------------------
    # Hover bars (4–5 samples)
    # -----------------------------
    bars = facility.get_kpi_bars()
    assert len(bars) >= 3, "Not enough bars rendered"

    for index, bar in enumerate(bars[:5], start=1):
        facility.hover_on_kpi_bar(bar)
        assert facility.is_barchart_tooltip_visible(), f"No tooltip on bar {index}"
        facility.reset_hover()

    print("✅ KPI Bar chart dropdown & hover validated")
