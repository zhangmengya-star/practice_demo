import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 隐式等待：设置一个等待时间，轮询查找（默认0.5秒）元素是否出现，如果没有出现就抛出异常；全局的
# 显式等待：在代码中定义等待条件，当条件发生时才继续执行代码
# WebDriverWait配合until()和until_not()方法，根据判断条件进行等待
# 程序每隔一段时间（默认为0.5秒）进行条件判断，如果条件成立，则执行下一步，否则继续等待，直到超过设置的最长时间
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]').click()
        '''
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1
        WebDriverWait(self.driver, 10).until(wait)
        '''
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
