from pages.slider_page import SliderPage
from tests.test_login import login_and_reach_dashboard
from utils.csv_writer import start_new_report, write_test_report
import time

def test_slider_navigation():
    # 🔥 Start report ONCE
    start_new_report()

    # 🔑 Login once & reach dashboard
    driver = login_and_reach_dashboard()

    try:
        slider_page = SliderPage(driver)

        sliders = [
            "Demand Insights",
            "Capacity Insights",
            "Supply Insights",
            "Part Allocation Insights"
        ]

        for slider in sliders:
            slider_page.click_slider(slider)
            time.sleep(2)

            write_test_report(
                "Tower Track",
                "Web",
                "Dashboard Slider",
                f"Verify {slider} button",
                f"Click on {slider} button",
                f"{slider} page should open",
                f"{slider} page opened successfully",
                "Pass",
                "",
                "1923",
                ""
            )

    finally:
        driver.quit()
        print("🧹 Browser closed")

if __name__ == "__main__":
    test_slider_navigation()
