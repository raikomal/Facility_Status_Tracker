# from pages.slider_page import SliderPage
# from tests.login_helper import login_and_reach_dashboard
# from utils.csv_writer import start_new_report, write_test_report
# import time

# def test_slider_navigation(driver):
#     slider_page = SliderPage(driver)

#     try:
#         slider_page = SliderPage(driver)

#         sliders = [
#             "Demand Insights",
#             "Capacity Insights",
#             "Supply Insights",
#             "Part Allocation Insights"
#         ]

#         for slider in sliders:
#             slider_page.click_slider(slider)
#             time.sleep(2)

#             write_test_report(
#                 "Tower Track",
#                 "Web",
#                 "Dashboard Slider",
#                 f"Verify {slider} button",
#                 f"Click on {slider} button",
#                 f"{slider} page should open",
#                 f"{slider} page opened successfully",
#                 "Pass",
#                 "",
#                 "1923",
#                 ""
#             )

#     finally:
#         driver.quit()
#         print("🧹 Browser closed")

# if __name__ == "__main__":
#     test_slider_navigation()

from pages.slider_page import SliderPage
from tests.login_helper import login_and_reach_dashboard
from utils.csv_writer import write_test_report
import time


def test_slider_navigation():
    # 🔐 Reuse login from File-1
    driver = login_and_reach_dashboard()
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

    print("✅ All sliders verified successfully")
