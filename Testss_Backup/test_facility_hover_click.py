from pages.slider_page import SliderPage
import time


def test_hover_and_click_facility_status_tracker(driver):
    slider = SliderPage(driver)

    # Step 1: Click Part Allocation Insights
    slider.click_slider("Part Allocation Insights")
    time.sleep(2)

    # Step 2: Hover + click Facility Status Tracker
    slider.hover_and_click_facility_status_tracker()
    time.sleep(3)   # visible pause for demo

    # No assertions – demo/navigation test only
    print("✅ Facility Status Tracker hover and click executed")
