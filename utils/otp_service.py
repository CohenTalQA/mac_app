from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

class OtpService:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_otp(self, timeout=30, interval=2):

        start_time = int(time.time() * 1000)

        while int(time.time() * 1000) - start_time < timeout * 1000:

            notifications = self.driver.execute_script("mobile: getNotifications")

            for n in notifications.get("statusBarNotifications", []):

                package = n.get("packageName")
                post_time = n.get("postTime")

                notification = n.get("notification", {})
                text = notification.get("text", "")

                if (
                        package == "com.samsung.android.messaging"
                        and post_time
                        and post_time >= start_time
                        and text
                        and "סיסמה חד פעמית שלך לאפליקציית מכבידנט" in text
                ):

                    otp_match = re.search(r"\d{6}", text)
                    if otp_match:
                        return otp_match.group()

            time.sleep(interval)

        raise Exception("OTP SMS not received")

        raise Exception("OTP SMS not received")

    def enter_otp(self, otp):
        otp_input = self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/login_otp_pinview")
            )
        )

        otp_input.send_keys(otp)
