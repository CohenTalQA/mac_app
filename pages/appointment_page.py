from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppointmentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def enter_appointment_page(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/entrance_index00")
            )
        )
        button.click()
    def open_new_appointment(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/maccabident_custom_button_text")
            )
        )
        button.click()
    def dent_test_appointment(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.maccabident.maccabidentAPP:id/appointment_card_layout").instance(0)')
            )
        )
        button.click()

    def regular_appointment(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.maccabident.maccabidentAPP:id/appointment_card_layout").instance(0)')
            )
        )
        button.click()
    def choose_city(self):
        clinic = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/chose_doctor_or_city")
            )
        )
        clinic.click()
    def select_city(self):
        clinic = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("אופקים")')
            )
        )
        clinic.click()
    def select_clinic(self):
        clinic = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "אופקים, רח' הרצל 36 ג', התור הפנוי הקרוב ביותר, בתאריך 29/03/2026,בשעה 19:45, לחץ פעמיים לבחירה, ")
            )
        )
        clinic.click()

    def choose_doctor(self):
        doctor = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.maccabident.maccabidentAPP:id/allDetails").instance(0)')
            )
        )
        doctor.click()

    def select_first_available_time(self):
        times = self.wait.until(
            EC.presence_of_all_elements_located(
                (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/hour_option")
            )
        )

        if times:
            times[0].click()

    def confirm_appointment(self):
        confirm = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/maccabident_custom_button_text")
            )
        )
        confirm.click()

    #com.maccabident.maccabidentAPP:id/maccabident_custom_button_text
    def finish_appointment(self):
        finish = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/maccabident_custom_button_text")
            )
        )
        finish.click()