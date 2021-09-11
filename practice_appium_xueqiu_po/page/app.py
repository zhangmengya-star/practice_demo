from appium import webdriver

from practice_appium_xueqiu_po.page.base_page import BasePage
from practice_appium_xueqiu_po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "Android"
            caps["deviceName"] = "test"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps['noReset'] = "true"
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(10)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> MainPage:
        return MainPage(self._driver)
