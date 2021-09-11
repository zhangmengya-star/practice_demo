import os

from practice_selenium_wechat_po.page.main_page import MainPage


class TestMain:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    def test_add_member(self):
        # # 方法一，在首页点击「添加成员」进入
        # self.main.goto_add_member().add_member()

        # 方法二，在首页点击「通讯录」，再点击「添加成员」进入
        address_book_page = self.main.goto_address_book()
        add_member_page = address_book_page.goto_add_member()
        add_member_page.add_member()
        assert address_book_page.is_exist_member('username')

    def test_delete_member(self):
        address_book_page = self.main.goto_address_book()
        address_book_page.delete_member('username')

