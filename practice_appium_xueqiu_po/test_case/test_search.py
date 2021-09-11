from practice_appium_xueqiu_po.page.app import App


class TestSearch:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_search(self):
        self.market_page = self.main.goto_market()
        self.search_page = self.market_page.goto_search()
        self.search_page.search()

    def teardown(self):
        pass
