from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class EnterLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_login(self):
        homepage_login = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/entrance_personal_link")
            )
        )

        homepage_login.click()

    def enter_id(self, user_id):
        id_field = self.wait.until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").text("מספר תעודת זהות")'
                )
            )
        )

        id_field.send_keys(user_id)

    def open_birth_picker(self):
        birth_field = self.wait.until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").text("תאריך לידה")'
                )
            )
        )

        birth_field.click()

    def pick_birth_day(self, current_day, target_day):
        day_element = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{current_day}")')
            )
        )
        day_element.click()
        day_element.clear()
        cleared_input_day = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().resourceId("android:id/numberpicker_input").instance(0)')
            )
        )
        cleared_input_day.send_keys(target_day)

        click_month = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().resourceId("android:id/numberpicker_input").instance(1)')
            )
        )
        click_month.click()

    def pick_birth_month(self, current_month, target_month):
        month_element = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{current_month}")')
            )
        )
        month_element.click()
        month_element.clear()
        cleared_input_month = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().resourceId("android:id/numberpicker_input").instance(1)')
            )
        )
        cleared_input_month.send_keys(target_month)

    def pick_birth_year(self, year, target_year):
        year_element = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH,
                 f'//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{year}"]')
            )
        )

        year_element.click()
        year_element.clear()
        # new UiSelector().resourceId("android:id/numberpicker_input").instance(2)
        cleared_input_year = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().resourceId("android:id/numberpicker_input").instance(2)')
            )
        )
        cleared_input_year.send_keys(target_year)

    def confirm_birth_date(self):
        confirm_button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "android:id/button1")
            )
        )

        confirm_button.click()

    # com.maccabident.maccabidentAPP:id/maccabident_custom_button_text "send code button"

    def click_send_code(self):
        send_code_button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, 'com.maccabident.maccabidentAPP:id/maccabident_custom_button_text')
            )
        )

        send_code_button.click()

    # collect verification code from sms notification and return driver.open_notifications()

    # def wait_for_otp(self, timeout=30, interval=2):
    #
    #     start_time = int(time.time() * 1000)
    #
    #     while int(time.time() * 1000) - start_time < timeout * 1000:
    #
    #         notifications = self.driver.execute_script("mobile: getNotifications")
    #
    #         for n in notifications.get("statusBarNotifications", []):
    #
    #             package = n.get("packageName")
    #             post_time = n.get("postTime")
    #
    #             notification = n.get("notification", {})
    #             text = notification.get("text", "")
    #
    #             if (
    #                     package == "com.samsung.android.messaging"
    #                     and post_time
    #                     and post_time >= start_time
    #                     and text
    #                     and "סיסמה חד פעמית שלך לאפליקציית מכבידנט" in text
    #             ):
    #
    #                 otp_match = re.search(r"\d{6}", text)
    #                 if otp_match:
    #                     return otp_match.group()
    #
    #         time.sleep(interval)
    #
    #     raise Exception("OTP SMS not received")
    #
    #     raise Exception("OTP SMS not received")
    #
    # def enter_otp(self, otp):
    #     otp_input = self.wait.until(
    #         EC.presence_of_element_located(
    #             (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/login_otp_pinview")
    #         )
    #     )
    #
    #     otp_input.send_keys(otp)
