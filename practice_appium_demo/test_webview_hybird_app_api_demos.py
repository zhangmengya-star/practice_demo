import time

from appium import webdriver


class TestWebviewWebAppApiDemos:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'true'
        desired_caps['appPackage'] = 'com.example.android.apis'
        desired_caps['appActivity'] = '.ApiDemos'
        desired_caps['chromedriverExecutable'] = '/Users/yuanmeng/software/app/chromedriver_74'
        desired_caps['noReset'] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_context(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Views").instance(0));'
        ).click()
        # 打印上下文
        print(self.driver.contexts)
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("WebView").instance(0));'
        ).click()
        # 打印上下文
        print(self.driver.contexts)
        # 进入webview页面，需要切换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.page_source)
        time.sleep(3)
