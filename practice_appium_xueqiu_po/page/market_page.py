from appium.webdriver.common.mobileby import MobileBy

from practice_appium_xueqiu_po.page.base_page import BasePage
from practice_appium_xueqiu_po.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID, 'com.xueqiu.android:id/action_search').click()
        return SearchPage(self._driver)
