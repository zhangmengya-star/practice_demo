from appium.webdriver.common.mobileby import MobileBy

from practice_appium_wechat_po.page.add_member import AddMember
from practice_appium_wechat_po.page.base_page import BasePage


class AddressBookPage(BasePage):
    def goto_add_member(self):
        # 点击「添加成员」
        self._driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        return AddMember(self._driver)
