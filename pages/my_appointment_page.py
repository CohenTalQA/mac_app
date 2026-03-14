from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyAppointmentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def open_my_appointment_page(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("entrance_rounded_btn_bg").instance(2)')
            )
        )
        button.click()

    def select_my_appointment(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("line").instance(0)')
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



