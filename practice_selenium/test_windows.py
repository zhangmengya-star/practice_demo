import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWindows:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    # 打开百度页面
    # 点击登录
    # 弹窗中点击“立即注册”，输入用户名和密码
    # 返回刚才的登录页，点击登录
    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        login_element = self.driver.find_element(By.CSS_SELECTOR, '#u1 > a')
        login_element.click()

        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        register_element = self.driver.find_element(By.LINK_TEXT, '立即注册')
        register_element.click()

        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        user_name_text = self.driver.find_element_by_id('TANGRAM__PSP_4__userName')
        user_name_text.send_keys('username')
        tel_text = self.driver.find_element_by_id('TANGRAM__PSP_4__phone')
        tel_text.send_keys('1380000000')

        time.sleep(1)

        self.driver.switch_to.window(windows[0])

        login_frame_button = self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn')
        login_frame_button.click()

        time.sleep(3)
