from selenium import webdriver
import time


class TestCsIndex:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.csindex.com.cn/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_csindex_xpath(self):
        self.driver.find_element_by_xpath('//*[@id="search_f"]').send_keys("中证银行")
        self.driver.find_element_by_xpath('//*[@id="s_submit_f"]').click()
        time.sleep(3)

        self.driver.find_element_by_xpath('//*[@id="itemContainer"]/tr[1]/td[1]/a').click()
        time.sleep(3)

    def test_csindex_css_selector(self):
        self.driver.find_element_by_css_selector('[id="search_f"]').send_keys("中证银行")
        self.driver.find_element_by_css_selector('[title="搜索"]').click()
        time.sleep(3)

        self.driver.find_element_by_css_selector('[id="itemContainer"]>tr:nth-child(1)>td:nth-child(1)').click()
        time.sleep(3)


