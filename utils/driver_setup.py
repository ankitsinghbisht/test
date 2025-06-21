from apnium import AndroidDriver

def create_driver():
    caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "app": "/path/to/your/app.apk",
        "automationName": "UiAutomator2"
    }
    return AndroidDriver("http://localhost:4723/wd/hub", caps)