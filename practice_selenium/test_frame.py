import time

from selenium import webdriver


class TestFrame:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

        self.driver.switch_to.frame('iframeResult')
        # # 另一种写法
        # self.driver.switch_to_frame('iframeResult')
        draggable_button = self.driver.find_element_by_id('draggable')
        print(draggable_button.text)

        # self.driver.switch_to.parent_frame()
        # 另一种写法
        self.driver.switch_to_default_content()
        run_button = self.driver.find_element_by_id('submitBTN')
        print(run_button.text)

        time.sleep(5)
