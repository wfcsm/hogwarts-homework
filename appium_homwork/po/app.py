from appium import webdriver

from appium_homwork.po.base_page import BasePage
from appium_homwork.po.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            des_caps = {
                'platformName': 'android',
                'deviceName': 'emulator-5554',
                # com.tencent.wework/.launch.WwMainActivity
                'appPackage': 'com.tencent.wework',
                'appActivity': '.launch.WwMainActivity',
                'platformVersion': '6.0',
                'noReset': True,
                # 'autoGrantPermissions': True
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        # pass

    def app_close(self):
        self.driver.quit()

    def go_to_main_page(self):
        # self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        return MainPage(self.driver)