import time

from selenium import webdriver


class TestWorkWechatBrowserReuse:
    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(3)


    def teardown(self):
        self.driver.quit()

    def test_wechat(self):
        self.driver.find_element_by_id('menu_contacts').click()
        print(self.driver.get_cookies())
        time.sleep(3)
