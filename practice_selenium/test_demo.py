from selenium import webdriver
import time


def test_open_baidu():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys('猿辅导')
    # time.sleep(3)
    driver.find_element_by_css_selector('[name="wd"]').send_keys('猿辅导')
    time.sleep(3)
