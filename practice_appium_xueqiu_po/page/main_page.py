from appium.webdriver.common.mobileby import MobileBy

from practice_appium_xueqiu_po.page.base_page import BasePage
from practice_appium_xueqiu_po.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        self.find(MobileBy.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
        return MarketPage(self._driver)
