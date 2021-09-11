from appium.webdriver.common.mobileby import MobileBy


def handle_black(func):
    def wrapper(*args, **kwargs):
        from practice_appium_xueqiu_po.page.base_page import BasePage
        _black_list = [
            (MobileBy.XPATH, '//*[@text="确定"]'),
            (MobileBy.XPATH, '//*[@text="下次再说"]'),
            (MobileBy.ID, 'com.xueqiu.android:id/iv_close')
        ]
        _max_num = 3
        _error_num = 0
        instance: BasePage = args[0]
        try:
            element = func(*args, **kwargs)
            return element
        except Exception as e:
            _error_num += 1
            if _error_num > _max_num:
                raise e
            instance._driver.implicitly_wait(1)
            for black in _black_list:
                elements = instance._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    instance._driver.implicitly_wait(10)
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
