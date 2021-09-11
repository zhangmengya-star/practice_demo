import os
from os import path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from practice_selenium_wechat_po.page.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member(self):
        # 上传头像
        # 显式等待
        self.wait_add_member_page_loaded()
        image_upload_button = self.find(By.CSS_SELECTOR, '.ww_icon_CameraWhiteSmall')
        image_upload_button.click()
        image = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/attachment/0.jpeg"
        self.find(By.CSS_SELECTOR, '.cropper_noImage input').send_keys(image)
        self.find(By.CSS_SELECTOR, '.js_save').click()

        # 姓名
        self.find(By.ID, 'username').send_keys('username')
        # 别名
        self.find(By.ID, 'memberAdd_english_name').send_keys('username')
        # 帐号
        self.find(By.ID, 'memberAdd_acctid').send_keys('username')
        #  性别选择"女"
        self.find(By.CSS_SELECTOR, '[value="2"]').click()
        # 手机号
        self.find(By.ID, 'memberAdd_phone').send_keys('11111111111')
        # 座机
        self.find(By.ID, 'memberAdd_telephone').send_keys('11111111111')
        # 地址
        self.find(By.ID, 'memberEdit_address').send_keys('11111111111')
        # 职务
        self.find(By.ID, 'memberAdd_title').send_keys('11111111111')
        # 取消勾选"通过邮件或短信发送企业邀请"
        send_invite_element = self.find(By.CSS_SELECTOR, '[name="sendInvite"]')
        if send_invite_element.is_selected():
            send_invite_element.click()

        # 点击保存按钮
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def wait_add_member_page_loaded(self):
        WebDriverWait(self._driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.ww_icon_CameraWhiteSmall')))
