import allure


@allure.feature('登录功能')
class TestLogin:

    @allure.step('打开网页')
    def open(self):
        print('打开网页')

    @allure.step('输入用户名')
    def get_user_name(self):
        print('输入用户名')

    @allure.step('输入密码')
    def get_user_password(self):
        print('输入密码')

    @allure.step('点击提交按钮')
    def submit(self):
        print('点击提交按钮')

    @allure.step('关闭网页')
    def close(self):
        print('关闭网页')

    @allure.story('测试登录成功')
    def test_login_success(self):
        self.open()
        self.get_user_name()
        self.get_user_password()
        self.submit()
        self.close()

    @allure.story('测试登录失败')
    def test_login_fail(self):
        with allure.step('打开网页'):
            print('打开网页')
        with allure.step('输入正确的用户名'):
            print('输入正确的用户名')
        with allure.step('输入错误的密码'):
            print('输入错误的密码')
        with allure.step('点击提交按钮'):
            print('点击提交按钮')
        with allure.step('关闭网页'):
            print('关闭网页')
            assert 1 == 2


@allure.feature('购物车')
class TestShoppingCart:

    @allure.story('加入购物车')
    def test_add_to_cart(self):
        print('浏览商品')
        print('选择商品')
        print('选择商品属性')
        print('加入购物车')

    @allure.story('删除购物车')
    def test_delete_shopping_cart(self):
        print('进入购物车')
        print('选择要删除的商品')
        print('进行商品删除')
        print('点击确定')
