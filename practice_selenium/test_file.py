import time
from os import path

from selenium import webdriver


class TestFile:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_file(self):
        # 在百度搜索首页，上传图片进行搜索
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_css_selector('.soutu-btn').click()
        self.driver.find_element_by_css_selector('.upload-pic').send_keys(
            path.dirname(__file__) + '/0.gif')
        time.sleep(3)
