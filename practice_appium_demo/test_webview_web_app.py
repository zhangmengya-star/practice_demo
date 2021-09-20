import time

from appium import webdriver


class TestWebviewWebApp:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'true'
        # desired_caps['appPackage'] = 'io.appium.android.apis'
        # desired_caps['appActivity'] = 'io.appium.android.apis.view.PopupMenu1'
        desired_caps['browserName'] = 'Browser'
        desired_caps['chromedriverExecutable'] = '/Users/myname/software/app/chromedriver_2.18'
        desired_caps['noReset'] = "true"
        # appium本身的设置就自带的，不需要额外添加，默认就是uiautomator2
        desired_caps['automationName'] = "uiautomator2"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_css_selector('#index-kw').send_keys('appium')
        time.sleep(10)
