from appium.webdriver.common.mobileby import MobileBy

from practice_appium_wechat_po.page.add_manual_page import AddManualPage
from practice_appium_wechat_po.page.base_page import BasePage


class AddMember(BasePage):
    def goto_add_manual(self):
        # 点击"手动输入添加"
        self._driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return AddManualPage(self._driver)
