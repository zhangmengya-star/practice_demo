from appium.webdriver.common.mobileby import MobileBy

from practice_appium_wechat_po.page.address_book_page import AddressBookPage
from practice_appium_wechat_po.page.base_page import BasePage


class MainPage(BasePage):

    def goto_address_book_page(self):
        # 点击「通讯录」
        self._driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return AddressBookPage(self._driver)
