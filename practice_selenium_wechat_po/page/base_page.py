from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _driver = None
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def __init__(self, driver: WebDriver = None, url=''):
        if driver is None:
            # 浏览器复用，终端输入的命令：Google\ Chrome --remote-debugging-port=9222
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
            if len(url) > 0:
                self._base_url = url

            self._driver.get(self._base_url)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
