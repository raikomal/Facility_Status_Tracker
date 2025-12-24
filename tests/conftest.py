import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from login_helper import login_and_reach_dashboard

@pytest.fixture(scope="session")
def driver():
    driver = login_and_reach_dashboard()
    yield driver
    driver.quit()
