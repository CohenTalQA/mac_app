from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


def wait_for_loader_to_disappear(driver):
    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located(
            (AppiumBy.ID, "maccabident_tooth_animation_view")
        )
    )