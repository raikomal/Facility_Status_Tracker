# from pages.slider_page import SliderPage
# from pages.facility_status_page import FacilityStatusPage
#
# # 🎥 DEMO MODE SPEED
# FacilityStatusPage.DEMO_DELAY = 5
#
#
# def test_demo_strategic_overview(driver):
#     slider = SliderPage(driver)
#     facility = FacilityStatusPage(driver)
#
#     print("\n🎥 DEMO MODE: Strategic Overview\n")
#
#     # -------------------------------------------------
#     # NAVIGATION
#     # -------------------------------------------------
#     slider.click_slider("Part Allocation Insights")
#     facility.demo_pause(1)
#
#     slider.hover_and_click_facility_status_tracker()
#     facility.demo_pause(1)
#
#     facility.click_strategic_overview()
#     facility.verify_strategic_overview_loaded()
#     facility.demo_pause(1)
#
#     # -------------------------------------------------
#     # MAP DEMO
#     # -------------------------------------------------
#     print("🗺️ Map hover demo")
#     facility.hover_multiple_map_circles(5)
#     facility.demo_pause(1)
#
#     # -------------------------------------------------
#     # KPI TABLE DEMO
#     # -------------------------------------------------
#     print("📊 KPI table demo")
#     facility.scroll_to_kpi_table()
#     facility.demo_pause(1)
#
#     facility.demo_hover_kpi_table_rows(5)
#     facility.demo_pause(1)
#
#
#     # -------------------------------------------------
#     # BAR CHART DEMO (SAFE)
#     # -------------------------------------------------
#     print("📈 KPI bar chart demo")
#     facility.switch_kpi_view("barchart")
#     facility.demo_pause(2)
#     # Move away from map SVG before bar chart
#     facility.driver.execute_script("window.scrollBy(0, 700)")
#     facility.demo_pause(1)
#
#     for i in range(5):
#         print(f"Hovering bar {i+1}")
#         facility.hover_kpi_bar_by_index(i)
#         facility.demo_pause(2)
#
#     print("\n✅ DEMO COMPLETED SUCCESSFULLY\n")
