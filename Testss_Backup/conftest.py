import pytest
from tests.login_helper import login_and_reach_dashboard
from utils.csv_writer import start_new_report


@pytest.fixture(scope="session", autouse=True)
def initialize_csv_report():
    """
    Initialize CSV report ONCE per test session
    """
    start_new_report()


@pytest.fixture(scope="session")
def driver():
    driver = login_and_reach_dashboard()
    yield driver
    driver.quit()
