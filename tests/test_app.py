import json
from datetime import datetime
from pathlib import Path

from pages.enter_login_page import EnterLoginPage
from pages.appointment_page import AppointmentPage
from pages.my_appointment_page import MyAppointmentPage
from utils.driver_factory import create_driver
from utils.popup_handler import close_popups_if_exist,second_option_popup_if_exist
from utils.otp_service import OtpService
from flows.login_flow import login_flow
from flows.create_appointment_flow import create_appointment_flow
from flows.edit_appointment_flow import edit_appointment_flow
from flows.cancel_appointment_flow import cancel_appointment_flow




def load_config():
    config_path = Path(__file__).resolve().parent.parent / "config" / "config.json"
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Load configuration
config = load_config()
flows = config["flows"]
user = config["user"]


def test_app():
    driver = create_driver()
    login_page = EnterLoginPage(driver)
    appointment_page = AppointmentPage(driver)
    my_appointment_page = MyAppointmentPage(driver)
    otp_service = OtpService(driver)
    # variables
    current_date = datetime.today()
    day = f"{current_date.day:02}"
    month = current_date.month
    # convert month number to month name in hebrew
    months = ["ינו׳", "פבר׳", "מרץ", "אפר׳", "מאי", "יוני", "יולי", "אוג׳", "ספט׳", "אוק׳", "נוב׳", "דצמ׳"]
    month = months[month - 1]
    year = current_date.year

    try:
        if flows["login"]:
            login_flow(login_page, otp_service, user, month, day, driver)

        if flows["create_appointment"]:
            create_appointment_flow(appointment_page)

        if flows["edit_appointment"]:
            edit_appointment_flow(my_appointment_page, appointment_page, driver)

        if flows["cancel_appointment"]:
            cancel_appointment_flow(my_appointment_page, appointment_page, driver)

        # login flow
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
        # new appointment flow
        # appointment_page.enter_appointment_page()
        # appointment_page.dent_test_appointment()
        # appointment_page.regular_appointment()
        # appointment_page.choose_city()
        # appointment_page.select_city()
        # appointment_page.select_clinic()
        # appointment_page.choose_doctor()
        # appointment_page.select_first_available_time()
        # appointment_page.confirm_appointment()
        # appointment_page.finish_appointment()
        # # edit appointment flow
        # my_appointment_page.open_my_appointment_page()
        # my_appointment_page.select_my_appointment()
        # my_appointment_page.edit_my_appointment()
        # second_option_popup_if_exist(driver)
        # appointment_page.select_first_available_time()
        # appointment_page.confirm_appointment()
        # appointment_page.finish_appointment()
        #cancel appointment flow
        # my_appointment_page.select_my_appointment()
        # my_appointment_page.cancel_my_appointment()
        # second_option_popup_if_exist(driver)
        # appointment_page.select_first_available_time()
        # appointment_page.confirm_appointment()
        # appointment_page.finish_appointment()
        # my_appointment_page.back_home()
    finally:
        driver.quit()