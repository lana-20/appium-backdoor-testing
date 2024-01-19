import time
from appium import webdriver
from appium.options.common import AppiumOptions

APPIUM = "http://localhost:4723"
APP = "https://github.com/cloudgrey-io/the-app/releases/download/v1.8.1/TheApp-v1.8.1.apk"
CAPS = {
    "platformName": "Android",
    "appium:options": {
        "platformVersion": "10",
        "deviceName": "Android Emulator",
        "automationName": "Espresso",
        "app": APP,
    }
}
OPTIONS = AppiumOptions().load_capabilities(CAPS)
driver = webdriver.Remote(
    command_executor=APPIUM,
    options=OPTIONS
)
try:
    time.sleep(1)
    script_args = {
        "target": "application",
        "methods": [{
                "name": "raiseToast",
                "args": [{
                        "value": "Toast raised by test script",
                        "type": "String"
                }]
        }]
    }
    driver.execute_script("mobile: backdoor", script_args)
    time.sleep(2)
except Exception as e:
    print(f"Error: {e}")
finally:
    if driver is not None:
        driver.quit()