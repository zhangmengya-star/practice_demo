from appium import webdriver

from practice_appium_wechat_po.page.base_page import BasePage
from practice_appium_wechat_po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps['noReset'] = "true"
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            caps['dontStopAppOnReset'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()
            self._driver.start_activity("com.tencent.wework", ".launch.WwMainActivity")

        self._driver.implicitly_wait(10)

        return self

    def close(self):
        self._driver.quit()

    def main(self):
        return MainPage(self._driver)
