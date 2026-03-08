from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Device"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.maccabident.maccabidentAPP"
    options.app_activity = "com.maccabi.dent.ui.entrance.EntranceActivity"
    options.no_reset = True
    options.new_command_timeout = 300

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver