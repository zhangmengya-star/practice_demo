'''通讯录页'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from practice_selenium_wechat_po.page.add_member_page import AddMemberPage
from practice_selenium_wechat_po.page.base_page import BasePage


class AddressBookPage(BasePage):
    def goto_add_member(self):
        # 显式等待
        self.wait_address_book_page_loaded()
        self.find(By.CSS_SELECTOR, '.ww_operationBar>a:nth-child(2)').click()
        return AddMemberPage(self._driver)

    # 判断员工是否在列表中,当前实现只判断了第一页
    def is_exist_member(self, member_name):
        # 显式等待
        self.wait_address_book_page_loaded()
        members_element = self._driver.find_elements(By.CSS_SELECTOR, '#member_list tr td:nth-child(2)')
        for i in members_element:
            if member_name == i.get_attribute("title"):
                return True
        return False

    def wait_address_book_page_loaded(self):
        # 显式等待，判断页面加载完成
        WebDriverWait(self._driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.ww_checkbox')))

    def delete_member(self, member_name):
        # 显式等待
        self.wait_address_book_page_loaded()
        members_element = self._driver.find_elements(By.CSS_SELECTOR, '#member_list tr td:nth-child(2)')
        member_check_box_element = self._driver.find_elements(By.CSS_SELECTOR, '#member_list tr td:nth-child(1) input')
        for i in range(len(members_element)):
            if member_name == members_element[i].get_attribute("title"):
                member_check_box_element[i].click()
        time.sleep(5)

