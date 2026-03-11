
from pages.my_appointment_page import MyAppointmentPage
from pages.appointment_page import AppointmentPage
from pages.enter_login_page import EnterLoginPage
from utils.otp_service import OtpService
from flows.login_flow import login_flow
from flows.create_appointment_flow import create_appointment_flow
from flows.edit_appointment_flow import edit_appointment_flow
from flows.cancel_appointment_flow import cancel_appointment_flow





def test_full_flow(driver, user, date_parts, config_data):

    login_page = EnterLoginPage(driver)
    appointment_page = AppointmentPage(driver)
    my_appointment_page = MyAppointmentPage(driver)
    otp_service = OtpService(driver)

    login_flow(
        login_page,
        otp_service,
        user,
        date_parts["month"],
        date_parts["day"],
        driver
    )

    create_appointment_flow(appointment_page, driver)

    edit_appointment_flow(my_appointment_page, appointment_page, driver)

    cancel_appointment_flow(my_appointment_page, appointment_page, driver)