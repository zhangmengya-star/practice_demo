import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestGestureUnlock:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'true'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.FlashActivity'
        desired_caps['noReset'] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_gesture_unlock(self):
        self.driver.find_element_by_id('cn.kmob.screenfingermovelock:id/setPatternLayout').click()
        # action = TouchAction(self.driver)
        # action.press(x=119, y=175).wait(200).move_to(x=361, y=177).wait(200).move_to(x=598, y=175).wait(200).move_to(
        #     x=598, y=419).wait(200).move_to(x=613, y=656).wait(200).release().perform()
        # time.sleep(5)

        action = TouchAction(self.driver)
        action.press(x=119, y=175).wait(200).release().perform()
        time.sleep(10)

