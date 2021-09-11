import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.CSS_SELECTOR, 'input[value="click me"]')
        element_double_click = self.driver.find_element(By.CSS_SELECTOR, 'input[value="dbl click me"]')
        element_right_click = self.driver.find_element(By.CSS_SELECTOR, 'input[value="right click me"]')
        action = ActionChains(self.driver)
        # 链式写法
        # action.click(element_click)
        # action.double_click(element_double_click)
        # action.context_click(element_right_click)
        # action.perform()

        # 分布式写法
        action.click(element_click).double_click(element_double_click).context_click(element_right_click).perform()
        time.sleep(3)

    # 鼠标移动到元素上
    def test_move_to_element(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_css_selector("#s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(3)

    # 将一个元素拖拽到另一个元素上
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        dragger_element = self.driver.find_element_by_id('dragger')
        drop_element = self.driver.find_element_by_xpath("//body/div[2]")
        action = ActionChains(self.driver)
        # 写法一
        # action.drag_and_drop(dragger_element, drop_element)
        # 写法二
        # action.click_and_hold(dragger_element).release(drop_element)
        # 写法三
        action.click_and_hold(dragger_element).move_to_element(drop_element)

        action.perform()
        time.sleep(3)

    def test_key(self):
        self.driver.get("http://sahitest.com/demo/label.htm")

        user_name_element = self.driver.find_element_by_xpath("/html/body/label[1]/input")

        # 将光标定位到文本框中国
        user_name_element.click()

        action = ActionChains(self.driver)

        # 在本文框中输入内容
        action.send_keys("hello")
        action.pause(3)

        # 键盘按下空格
        action.send_keys(Keys.SPACE)
        action.pause(3)

        # 在文本框中输入内容
        action.send_keys("world!")
        action.pause(3)

        # 键盘按下删除键
        action.send_keys(Keys.BACK_SPACE)
        action.pause(3)

        # 鼠标键按下command+c,当前使用的电脑是mac
        action.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND)
        action.pause(3)

        action.perform()

        time.sleep(3)

