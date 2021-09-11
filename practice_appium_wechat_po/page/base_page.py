from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _black_list = [
        (MobileBy.XPATH, "//*[@text='确认']"),
        (MobileBy.XPATH, "//*[@text='下次再说']"),
        (MobileBy.XPATH, "//*[@text='确定']"),
    ]
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            self._error_num = 0
            return element
        except Exception as e:
            # 缩小隐式等待时间，提高运行速度
            self._driver.implicitly_wait(1)
            self._error_num += 1
            if self._error_num > self._max_num:
                raise e
            for ele in self._black_list:
                ele_list = self._driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    # 恢复隐式等待时间
                    self._driver.implicitly_wait(10)
                    return self.find(locator, value)

            raise e
