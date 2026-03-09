from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyAppointmentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def open_appointment_page(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.maccabident.maccabidentAPP:id/entrance_rounded_btn_bg").instance(2)')
            )
        )
        button.click()

    def select_appointment_type(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.maccabident.maccabidentAPP:id/line").instance(0)')
            )
        )
        button.click()
    def edit_appointment_type(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, 'com.maccabident.maccabidentAPP:id/edit_button')
            )
        )
        button.click()





