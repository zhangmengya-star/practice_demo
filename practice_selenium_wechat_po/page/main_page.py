import time

from selenium.webdriver.common.by import By

from practice_selenium_wechat_po.page.add_member_page import AddMemberPage
from practice_selenium_wechat_po.page.address_book_page import AddressBookPage
from practice_selenium_wechat_po.page.base_page import BasePage


class MainPage(BasePage):

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, '.ww_indexImg_AddMember').click()
        return AddMemberPage(self._driver)

    def goto_address_book(self):
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        return AddressBookPage(self._driver)
