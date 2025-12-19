import csv
import os
from datetime import datetime

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

# 🔑 UNIQUE FILE NAME PER RUN
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
CSV_PATH = f"{REPORT_DIR}/login_test_results_{TIMESTAMP}.csv"

HEADER = [
    "Project",
    "Application",
    "Micro_Application",
    "Test_Case_Title",
    "Test_Description",
    "Expected_Result",
    "Actual_Result",
    "Status",
    "Remark",
    "Task_ID",
    "Ticket_ID"
]

def start_new_report():
    with open(CSV_PATH, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)

def write_test_report(
    project,
    application,
    micro_application,
    title,
    description,
    expected_result,
    actual_result,
    status,
    remark,
    task_id,
    ticket_id
):
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow([
            project,
            application,
            micro_application,
            title,
            description,
            expected_result,
            actual_result,
            status,
            remark,
            task_id,
            ticket_id
        ])
