from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from practice_appium_xueqiu_po.page.wrapper import handle_black


class BasePage:
    _black_list = [
        (MobileBy.XPATH, '//*[@text="确定"]'),
        (MobileBy.XPATH, '//*[@text="下次再说"]'),
    ]
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, locator, value):
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def finds(self, locator, value):
        if isinstance(locator, tuple):
            self._driver.find_elements(*locator)
        else:
            self._driver.find_elements(locator, value)

    def find_1(self, locator, value):
        try:
            if isinstance(locator, tuple):
                self._driver.find_element(*locator)
            else:
                self._driver.find_element(locator, value)
        except Exception as e:
            self._error_num += 1
            if self._error_num > self._max_num:
                raise e
            self._driver.implicitly_wait(1)
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    self._driver.implicitly_wait(10)
                    return self.find_1(locator, value)
            raise e
