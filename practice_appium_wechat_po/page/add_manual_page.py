import time

from appium.webdriver.common.mobileby import MobileBy

from practice_appium_wechat_po.page.base_page import BasePage


class AddManualPage(BasePage):
    def add(self):
        # 输入姓名
        self.find(MobileBy.XPATH,
                                  '//*[contains(@text,"姓名")]/..//*[@class="android.widget.EditText"]').send_keys(
            'username2')
        # 选择性别
        self.find(MobileBy.XPATH,
                                  '//*[@text="性别"]/..//*[@class="android.widget.RelativeLayout"]').click()
        self.find(MobileBy.XPATH, '//*[@resource-id="android:id/content"]/..//*[@text="女"]').click()
        # 输入手机号
        self.find(MobileBy.XPATH,
                                  '//*[contains(@text,"手机号")]').send_keys(
            '13800000001')
        # 输入邮箱
        self.find(MobileBy.XPATH,
                                  '//*[contains(@text,"邮箱")]/..//*[@class="android.widget.EditText"]').send_keys(
            '2406715954@qq.com')
        # 点击「保存」
        self.find(MobileBy.XPATH, '//*[@text="保存" and @class="android.widget.TextView"]').click()

        time.sleep(5)


