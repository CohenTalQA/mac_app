from utils.popup_handler import close_popups_if_exist


def login_flow(login_page, otp_service, user, month, day, driver):

    login_page.click_login()
    login_page.enter_id(user["id"])
    login_page.open_birth_picker()

    login_page.pick_birth_year("2010", user["year"])
    login_page.pick_birth_month(month, user["month"])
    login_page.pick_birth_day(day, user["day"])

    login_page.confirm_birth_date()
    login_page.click_send_code()

    otp = otp_service.wait_for_otp()
    otp_service.enter_otp(otp)

    close_popups_if_exist(driver, 3)