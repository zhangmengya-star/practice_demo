import allure


class TestLink:
    # 关联链接
    @allure.link("https://www.baidu.com/")
    def test_link_1(self):
        print("test_link_1")

    # 关联链接
    @allure.link("https://www.baidu.com/", name="百度一下")
    def test_link_2(self):
        print("test_link_2")

    # 关联测试用例
    @allure.testcase("http://news.baidu.com/", "这里是测试用例的地址")
    def test_case(self):
        print("test_case")

    # 关联bug
    @allure.issue("http://www.myissue.com/123", "这里是一个bug链接")
    def test_issue(self):
        print("test_issue")

    # 关联网页
    # 用法：allure.attach(body,name,attachment_type,extension)
    def test_attach_html(self):
        print("test_attach_html")
        allure.attach('<head></head><body>首页</body>', '这是错误页的结果信息', allure.attachment_type.HTML)

    # 关联图片
    # 用法：allure.attach.file(source,name,attachment_type,extension)
    def test_attach_file(self):
        print("test_attach_file")
        allure.attach.file('./1.jpg', name='这是一个图片', attachment_type=allure.attachment_type.JPG)
