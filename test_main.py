import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.options.android import UiAutomator2Options


capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.quit()


def test_find_battery(driver) -> None:
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()
    sleep(5)
