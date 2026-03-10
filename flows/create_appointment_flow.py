from utils.loader_handler import wait_for_loader_to_disappear

def create_appointment_flow(appointment_page,driver):

    appointment_page.enter_appointment_page()
    appointment_page.dent_test_appointment()
    appointment_page.regular_appointment()
    appointment_page.choose_city()
    appointment_page.select_city()
    wait_for_loader_to_disappear(driver)
    appointment_page.select_clinic()
    appointment_page.choose_doctor()
    appointment_page.select_first_available_time()
    appointment_page.confirm_appointment()
    wait_for_loader_to_disappear(driver)
    appointment_page.finish_appointment()


