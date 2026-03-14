from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AppointmentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_appointment_page(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "entrance_index00")
            )
        )
        button.click()

    def dent_test_appointment(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("בדיקת רופא/ת שיניים")')
            )
        )
        button.click()

    def regular_appointment(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().text("ביקור רגיל")')
            )
        )
        button.click()

    def choose_city(self):
        clinic = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "chose_doctor_or_city")
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
            EC.presence_of_element_located( (AppiumBy.ID,'appointment_texts_layout' )
            )
        )
        print(clinic)
        clinic.click()

    def choose_doctor(self):
        doctor = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().resourceId("allDetails").instance(0)')
            )
        )
        doctor.click()

    def select_first_available_time(self):
        times = self.wait.until(
            EC.presence_of_all_elements_located(
                (AppiumBy.ID, "hour_option")
            )
        )

        if times:
            times[0].click()

    def confirm_appointment(self):
        confirm = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "maccabident_custom_button_text")
            )
        )
        confirm.click()

    # maccabident_custom_button_text
    def finish_appointment(self):
        finish = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().resourceId("maccabident_custom_button_text").text("סיום")')
            )
        )
        finish.click()
