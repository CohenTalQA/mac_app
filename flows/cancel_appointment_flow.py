
from utils.popup_handler import second_option_popup_if_exist
from utils.loader_handler import wait_for_loader_to_disappear
def cancel_appointment_flow(my_appointment_page,appointment_page, driver):
    my_appointment_page.select_my_appointment()
    my_appointment_page.cancel_my_appointment()
    # Handle the second option popup if it appears
    second_option_popup_if_exist(driver)
    wait_for_loader_to_disappear(driver)
    my_appointment_page.back_home()
