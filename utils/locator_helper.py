from appium.webdriver.common.appiumby import AppiumBy


def id_locator(driver, element_id):
    package = driver.current_package
    return (AppiumBy.ID, f"{package}:id/{element_id}")


def ui_selector(driver, element_id, instance=None):
    package = driver.current_package

    locator = f'new UiSelector().resourceId("{package}:id/{element_id}")'

    if instance is not None:
        locator += f".instance({instance})"

    return (AppiumBy.ANDROID_UIAUTOMATOR, locator)

