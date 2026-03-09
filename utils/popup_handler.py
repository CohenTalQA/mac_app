from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def close_popups_if_exist(driver, max_attempts=5):
    for _ in range(max_attempts):
        try:
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/general_popup_x_button")
                )
            )

            close_button.click()
            print("Popup closed")

            time.sleep(1)  # נותן זמן לפופאפ הבא להופיע

        except TimeoutException:
            break

def second_option_popup_if_exist(driver):
    try:
        second_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "com.maccabident.maccabidentAPP:id/general_popup_center_button")
            )
        )
        second_button.click()
        print("Second popup closed")

    except TimeoutException:
        print("Second popup not found")
