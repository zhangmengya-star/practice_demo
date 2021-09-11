from appium.webdriver.common.mobileby import MobileBy

from practice_appium_xueqiu_po.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.find(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
