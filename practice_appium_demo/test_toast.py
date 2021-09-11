import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'true'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.view.PopupMenu1'
        desired_caps['noReset'] = "true"
        # appium本身的设置就自带的，不需要额外添加，默认就是uiautomator2
        desired_caps['automationName'] = "uiautomator2"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Make a Popup!').click()
        self.driver.find_element(MobileBy.ID, 'android:id/title').click()
        # 获取页面源码
        # print(self.driver.page_source)
        # 第一种获取toast方式
        print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        # 第二种获取toast方式
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "Clicked popup")]').text)
