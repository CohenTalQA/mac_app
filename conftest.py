import json
from pathlib import Path
import os
import pytest
from pages.appointment_page import AppointmentPage
from pages.my_appointment_page import MyAppointmentPage
from pages.enter_login_page import EnterLoginPage
from utils.driver_factory import create_driver
from datetime import datetime


@pytest.fixture
def driver(config_data):
    environment = config_data["environment"]
    driver = create_driver(environment)
    yield driver
    driver.quit()


@pytest.fixture
def appointment_page(driver):
    return AppointmentPage(driver)


@pytest.fixture
def my_appointment_page(driver):
    return MyAppointmentPage(driver)


@pytest.fixture
def login_page(driver):
    return EnterLoginPage(driver)


@pytest.fixture
def config_data(environment):

    if environment == "test":
        config_file = "config_test.json"

    elif environment == "prod":
        config_file = "config_prod.json"

    else:
        raise ValueError(f"Unknown environment: {environment}")

    config_path = Path(__file__).resolve().parent / "config" / config_file

    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture
def user(config_data):
    return config_data["user"]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            file_name = datetime.now().strftime("screenshots/%Y%m%d_%H%M%S.png")
            driver.save_screenshot(file_name)


@pytest.fixture
def date_parts():
    current_date = datetime.today()
    months = ["ינו׳", "פבר׳", "מרץ", "אפר׳", "מאי", "יוני", "יולי", "אוג׳", "ספט׳", "אוק׳", "נוב׳", "דצמ׳"]

    return {
        "day": f"{current_date.day:02}",
        "month": months[current_date.month - 1],
        "year": current_date.year,
    }

@pytest.fixture
def environment(request):
    return request.config.getoption("--env")

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="test",
        help="Environment to run tests against (test or prod)"
    )
