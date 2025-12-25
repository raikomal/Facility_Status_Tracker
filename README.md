Tower Track Automation Framework

Automation test framework for Tower Track – Facility Status Tracker using Selenium + PyTest.
This project validates Strategic Overview dashboards, including Map, KPI Cards, KPI Table, and Bar Chart interactions, with structured CSV reporting.

📌 Project Objective

The goal of this framework is to:

Automate end-to-end UI validation of Tower Track dashboards

Verify critical business KPIs

Ensure interactive charts (Highcharts) behave correctly

Generate clear CSV-based execution reports

Provide a scalable structure for future automation

🧱 Tech Stack

Python 3.14

Selenium WebDriver

PyTest

Highcharts (SVG handling)

CSV Reporting

GitHub Actions ready (future)

📁 Project Structure
Tower_Track/
│
├── pages/
│   ├── slider_page.py
│   ├── facility_status_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_strategic_overview_flow.py
│
├── utils/
│   ├── csv_writer.py
│   ├── alert_handler.py
│   ├── backend_check.py
│   ├── dom_waiter.py
│
├── reports/
│   └── login_test_results_YYYYMMDD_HHMMSS.csv
│
├── pytest.ini
├── requirements.txt
└── README.md

✅ Automated Test Coverage
1️⃣ Login Validation

Valid credentials login

Alert handling

Dashboard verification

2️⃣ Strategic Overview Page

Page load verification via Highcharts SVG

DOM stability handling

3️⃣ KPI Cards (Top Summary)

Overall Fulfillment Rate

Overall Reallocation Rate

Overall Misallocation Rate

4️⃣ Facility Map (Highcharts MapBubble)

Map bubble detection

Tooltip hover validation

Facility-level fulfillment rate

5️⃣ Facility KPI Table

Facility list validation

Misallocation rate extraction

Row hover behavior

6️⃣ Bar Chart (Reallocation Rate)

Bar detection

Tooltip hover validation

Chart stability without animation issues

📊 Reporting

CSV report generated per execution

Each step logged using write_test_report()

Includes:

Module

Scenario

Action

Expected vs Actual

Status (Pass / Fail)

Test Case ID

📂 Reports are stored in:

reports/

▶️ How to Run Tests
🔹 Install Dependencies
pip install -r requirements.txt

🔹 Run Strategic Overview Test
pytest tests/test_strategic_overview_flow.py -s

🔹 Run All Tests
pytest -s

🧠 Key Automation Design Decisions

Page Object Model (POM) for maintainability

Single DOM wait for Highcharts (prevents timeout loops)

Animation-safe chart handling

No hard-coded sleeps except minimal Highcharts stabilization

Explicit CSV logging for every business step

🛠 Utilities Explained
Utility	Purpose
csv_writer.py	Structured CSV reporting
alert_handler.py	Auto-handle browser alerts
dom_waiter.py	DOM stability checks
backend_check.py	Backend API validation (optional)
⚠️ Known Limitations

Highcharts tooltips are visual, not DOM nodes
→ Hover validation is behavior-based

Backend API checks are optional and environment-dependent

🔮 Future Enhancements (Planned)

Screenshot capture on failure

Allure / HTML report integration

CI pipeline (GitHub Actions)

Cross-browser execution

Parallel execution (pytest-xdist)

Sankey chart automation

👤 Maintainer

Komal Rai
Automation & QA Engineer
GitHub: https://github.com/raikomal

✅ Status

🟢 Stable
✔ Map hover working
✔ KPI table validated
✔ Bar chart hover working
✔ CSV reporting functional
