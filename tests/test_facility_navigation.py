from pages.slider_page import SliderPage


def test_facility_status_tracker_navigation(driver):
    slider = SliderPage(driver)

    # ===============================
    # SESSION-SAFE NAVIGATION
    # ===============================
    if "Part Allocation Insights" not in driver.page_source:
        slider.click_slider("Part Allocation Insights")

    slider.hover_and_click_facility_status_tracker()

    # ===============================
    # VALIDATION
    # ===============================
    assert "facility" in driver.current_url.lower()
