import allure


@allure.feature('登录模块')
class TestLogin():
    @allure.story('登录成功')
    @allure.testcase(url='https:www.baidu.com',name='百度链接')
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_success(self):
        with allure.step('步骤1：打开应用'):
            print('打开应用')
        with allure.step('步骤2：进入登录页面'):
            print('登录页面')
        with allure.step('步骤3：输入用户名和密码'):
            print('输入用户名和密码')
        print('这是登录：测试用例，登录成功')
        pass

    @allure.story('登录失败')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success_a(self):
        print('这是登录：测试用例，登录失败')
        pass

    @allure.story('用户名缺失')
    @allure.severity(allure.severity_level.MINOR)
    def test_login_success_b(self):
        print('用户名缺失')
        pass

    @allure.story('密码缺失')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_failure(self):
        with allure.step('点击用户名'):
            print('输入用户名')
        with allure.step('点击密码'):
            print('输入密码')
        with allure.step('点击登录'):
            print('点击登录')
        with allure.step('点击登录之后，登录失败'):
            assert '1'==1
            print('登录失败')
        pass

    @allure.story('登录失败')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_login_failure_a(self):
        print('这是登录：测试用例，登录失败')
        pass