import allure


@allure.severity(allure.severity_level.NORMAL)
def test_demo_1():
    print('test_demo_1')


@allure.severity(allure.severity_level.CRITICAL)
def test_demo_2():
    print('test_demo_2')


@allure.severity(allure.severity_level.NORMAL)
def test_demo_3():
    print('test_demo_3')


@allure.severity(allure.severity_level.MINOR)
def test_demo_4():
    print('test_demo_4')
