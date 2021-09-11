import time

from appium.webdriver.common.mobileby import MobileBy

from practice_appium_wechat_po.page.app import App
from practice_appium_wechat_po.page.main_page import MainPage


class TestMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_add_member(self):
        self.main.goto_address_book_page().goto_add_member().goto_add_manual().add()

    def teardown(self):
        pass
        #self.main.quit()

