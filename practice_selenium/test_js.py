import time

from selenium import webdriver


class TestJs:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(6)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    # 在百度输入框中输入"selenium"，并点击
    # 搜索结果页，切换到第二页
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id('kw').send_keys('selenium')
        # self.driver.find_element_by_id('su').click()
        # 使用js进行元素定位
        search_element = self.driver.execute_script("return document.getElementById('su')")
        search_element.click()

        # 执行js，页面滑动到底部
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        self.driver.find_element_by_css_selector('#page > div > a.n').click()
        time.sleep(3)

        # 输出页面的一些信息，js语句前添加 return
        print(self.driver.execute_script('return document.title'))
        print(self.driver.execute_script('return JSON.stringify(performance.timing)'))
        # 执行多条js语句，多条js语句用分号隔开
        print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))

    # 修改时间控件里的值
    def test_js_time(self):
        self.driver.get('https://www.12306.cn/index/')
        time.sleep(1)
        js = "a = document.getElementById('train_date');a.removeAttribute('readonly');a.value='2021-03-14'"
        self.driver.execute_script(js)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        time.sleep(3)

        # # 可以不用去掉readonly属性
        # self.driver.get('https://www.12306.cn/index/')
        # time.sleep(1)
        # js = "a = document.getElementById('train_date');a.value='2021-03-14'"
        # self.driver.execute_script(js)
        # print(self.driver.execute_script("return document.getElementById('train_date').value"))
        # time.sleep(3)
