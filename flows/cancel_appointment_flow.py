
from utils.popup_handler import second_option_popup_if_exist

def cancel_appointment_flow(my_appointment_page,appointment_page, driver):
    from flows.create_appointment_flow import create_appointment_flow
    my_appointment_page.select_my_appointment()
    my_appointment_page.cancel_my_appointment()
    # Handle the second option popup if it appears
    second_option_popup_if_exist(driver)
    my_appointment_page.back_home()

    # my_appointment_page.select_my_appointment()
    # my_appointment_page.cancel_my_appointment()
    # second_option_popup_if_exist(driver)
