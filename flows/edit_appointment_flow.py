from utils.popup_handler import second_option_popup_if_exist
from utils.loader_handler import wait_for_loader_to_disappear


def edit_appointment_flow(my_appointment_page, appointment_page, driver):

    my_appointment_page.open_my_appointment_page()
    my_appointment_page.select_my_appointment()
    my_appointment_page.edit_my_appointment()
    second_option_popup_if_exist(driver)
    appointment_page.select_first_available_time()
    appointment_page.confirm_appointment()
    wait_for_loader_to_disappear(driver)
    appointment_page.finish_appointment()