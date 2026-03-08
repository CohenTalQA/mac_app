import json
from datetime import datetime
from pathlib import Path

from pages.enter_login_page import EnterLoginPage
from pages.appointment_page import AppointmentPage
from utils.driver_factory import create_driver
from utils.popup_handler import close_popups_if_exist
from utils.otp_service import OtpService

def load_config():
    config_path = Path(__file__).resolve().parent.parent / "config" / "config.json"
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


def test_login():
    config = load_config()
    user = config["user"]

    driver = create_driver()
    login_page = EnterLoginPage(driver)
    appointment_page = AppointmentPage(driver)
    otp_service = OtpService(driver)
    current_date = datetime.today()
    # date format is dd/mm/yyyy

    # convert to number with leading zero if needed
    day = f"{current_date.day:02}"
    month = current_date.month
    # convert month number to month name in hebrew
    months = ["ינו׳", "פבר׳", "מרץ", "אפר׳", "מאי", "יוני", "יולי", "אוג׳", "ספט׳", "אוק׳", "נוב׳", "דצמ׳"]
    month = months[month - 1]
    year = current_date.year
    try:
        # login_page.click_login()
        # login_page.enter_id(user["id"])
        # login_page.open_birth_picker()
        # login_page.pick_birth_year("2010",user["year"]) # think how to fix this hardcoded year, maybe add it to the config file
        # login_page.pick_birth_month(str(month),user["month"])
        # login_page.pick_birth_day(str(day),user["day"])
        # login_page.confirm_birth_date()
        # login_page.click_send_code()
        # otp = otp_service.wait_for_otp()
        # otp_service.enter_otp(otp)
        # close_popups_if_exist(driver,3)
        # appointment_page.enter_appointment_page()
        # appointment_page.open_new_appointment()
        # appointment_page.dent_test_appointment()
        # appointment_page.regular_appointment()
        # appointment_page.choose_city()
        # appointment_page.select_city()
        # appointment_page.select_clinic()
        # appointment_page.choose_doctor()
        # appointment_page.select_first_available_time()
        # appointment_page.confirm_appointment()
        # appointment_page.finish_appointment()

    finally:
        driver.quit()