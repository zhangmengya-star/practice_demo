import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebviewHybirdAppXueqiu:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'true'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['chromedriverExecutable'] = '/Users/yuanmeng/software/app/chromedriver_74'
        desired_caps['noReset'] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_open_account(self):
        print(self.driver.contexts)
        # 点击"交易"进入webview页面
        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        print(self.driver.contexts)
        # 切换context
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.window_handles)
        open_account_locator = (MobileBy.CSS_SELECTOR, '.trade_home_onsale-container_Pgr')
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(open_account_locator))
        self.driver.find_element(*open_account_locator).click()

        print(self.driver.window_handles)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

        submit_button_locator = (MobileBy.CSS_SELECTOR, '.form > div[class="btn-submit"]')
        WebDriverWait(self.driver, 40).until(
            expected_conditions.element_to_be_clickable(submit_button_locator))
        self.driver.find_element(MobileBy.CSS_SELECTOR, '#phone-number').send_keys('12345678901')

        time.sleep(10)




