import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestElementOperator:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'true'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        '''
        案例:
            打开「雪球」应用首页
            定位首页的搜索框
            判断搜索框是否可用，并查看搜索框name属性值
            打印搜索框这个元素的左上角坐标和它的宽高
            向搜索框输入 阿里巴巴
            判断 阿里巴巴 是否可见
            如果可见，打印“搜索成功”，如果不可见，打印“搜索失败”
        :return:
        '''
        # time.sleep(5)
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        # time.sleep(5)
        search_element = self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text')
        # 判断元素是否可用
        print(search_element.is_enabled())
        # 获取文本
        print(search_element.text)
        # 获取坐标
        print(search_element.location)
        # 获取尺寸
        print(search_element.size)
        # 向输入框输入 阿里巴巴
        search_element.send_keys('阿里巴巴')
        # time.sleep(5)

        search_result_element = self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        # 判断 阿里巴巴 是否可见
        if search_result_element.is_displayed() == True:
            print('搜索成功')
        else:
            print('搜索失败')
        time.sleep(10)

    def test_page_slide(self):
        # 为了看清楚变化
        time.sleep(20)
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x = int(width / 2)
        y_start = int(height * 0.8)
        y_end = int(height * 0.2)
        action.press(x=x, y=y_start).wait(200).move_to(x=x, y=y_end).wait(200).release().perform()
        time.sleep(5)

    def test_stock_price(self):
        # 点击输入框
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        # 向输入框输入 阿里巴巴
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        # 点击第一个搜索结果
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        # 获取股票价格，使用显式等待
        price_locator = (
        MobileBy.XPATH, '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(price_locator))
        # 写法二，使用lambda表达式
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*price_locator))
        stock_price = self.driver.find_element(*price_locator).text
        print(stock_price)
        time.sleep(10)

    def test_login(self):
        # 点击我的，进入到个人信息页面
        # 点击登录，进入到登录页面
        # 输入用户名，输入密码
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("我的").resourceId("com.xueqiu.android:id/tab_name")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录雪球")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('username')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('password')
        time.sleep(5)

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("安娜2012").instance(0));'
        ).click()
