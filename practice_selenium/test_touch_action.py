import time

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_scroll_button(self):
        """
            打开百度
            在搜索框中输入'selenium测试'
            通过TouchAction点击搜索框
            滑动到底部，点击下一页
            关闭chrome
        """
        self.driver.get('https://www.baidu.com/')
        input_element = self.driver.find_element(By.ID, 'kw')
        input_element.send_keys('selenium测试')
        button_element = self.driver.find_element(By.ID, 'su')
        button_element.click()

        action = TouchActions(self.driver)
        action.scroll_from_element(button_element, 0, 10000)
        action.perform()

        next_element = self.driver.find_element_by_css_selector('#page > div > a.n')
        next_element.click()

        time.sleep(3)
