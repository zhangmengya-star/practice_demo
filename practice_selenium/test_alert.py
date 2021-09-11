import time

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestAlert:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 切换至iframeResult中
        self.driver.switch_to.frame('iframeResult')
        # 将"请拖拽我！"拖动到"请放置到这里！"
        draggable_element = self.driver.find_element_by_id('draggable')
        droppable_element = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable_element, droppable_element)
        action.perform()
        time.sleep(2)

        # 切换至弹窗并点击「确定」
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()
        time.sleep(2)

        self.driver.switch_to_default_content()
        # 点击「点击运行」按钮
        self.driver.find_element_by_id('submitBTN').click()
        time.sleep(3)

