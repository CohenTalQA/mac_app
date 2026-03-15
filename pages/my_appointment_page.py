from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locator_helper import ui_selector, id_locator

class MyAppointmentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def open_my_appointment_page(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                ui_selector(self.driver, 'entrance_rounded_btn_bg', instance=2))
        )
        button.click()


 # new UiSelector().resourceId("line").instance(0)
    def select_my_appointment(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (ui_selector(self.driver, 'line', instance=0))
            )
        )
        button.click()
    def edit_my_appointment(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, 'edit_button')
            )
        )
        button.click()

    def cancel_my_appointment(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, 'cancel_button')
            )
        )
        button.click()

    def back_home(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID,'maccabident_custom_button_text')
            )
        )
        button.click()



