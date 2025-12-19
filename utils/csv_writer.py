import csv
import os

CSV_PATH = "reports/login_test_results.csv"

def write_result(test_name, status, message):
    file_exists = os.path.isfile(CSV_PATH)

    with open(CSV_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Test Name", "Status", "Message"])

        writer.writerow([test_name, status, message])
