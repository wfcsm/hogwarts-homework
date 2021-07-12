from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions


class TestPunchCard:
    def setup(self):
        des_caps={
            'platformName': 'android',
            'deviceName': 'emulator-5554',
            # com.tencent.wework/.launch.WwMainActivity
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.WwMainActivity',
            'platformVersion': '6.0',
            'noReset': True,
            # 'autoGrantPermissions': True
            "settings[waitForIdleTimeout]": 0
        }
        # http://127.0.0.1:4444/wd/hub
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)
        # pass

    def teardown(self):
        pass

    def test_punch_card(self):
        self.driver.find_element_by_xpath('//*[@text="工作台"]').click()

        # 重要代码
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).\
                                 instance(0)).scrollIntoView(new UiSelector().\
                                 text("打卡").instance(0));').click()
        target=self.driver.find_elements_by_id('com.android.packageinstaller:id/dialog_container')
        # is_existence=expected_conditions.visibility_of_element_located((MobileBy.ID,'com.android.packageinstaller:id/dialog_container'))
        # print(is_existence)
        if target:
            self.driver.find_element_by_xpath('//*[@text="允许"]').click()
            # self.driver.find_element_by_xpath('//*[@text="拒绝"]').click()
        self.driver.find_element_by_xpath('//*[@text="外出打卡"]').click()
        self.driver.find_element_by_xpath('//*[contains(@text,"次外出")]').click()

        pass