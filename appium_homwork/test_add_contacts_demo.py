import time

import faker
from appium import webdriver


class TestAddContacts:
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'deviceName': 'emulator-5554',
            # com.tencent.wework/.launch.WwMainActivity
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.WwMainActivity',
            'platformVersion': '6.0',
            # 'noReset': True,
            'autoGrantPermissions': True

        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)
        # pass
    def teardown(self):
        time.sleep(3)
        # self.driver.quit()
        pass

    def test_add(self):
        # pass
        fake = faker.Factory().create('zh_CN')
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        # 需要加滑动查找
        self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        self.driver.find_element_by_xpath('//*[contains(@text,"手动输入添加")]').click()
        # 姓名
        self.driver.find_element_by_xpath('//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(fake.name())
        self.driver.find_element_by_xpath('//*[contains(@text,"手机")]/../android.widget.EditText').send_keys(fake.phone_number())
        self.driver.find_element_by_xpath('//*[@text="设置部门"]').click()
        self.driver.find_element_by_xpath('//*[contains(@text,"确定")]').click()
        # 取消自动发送邀请
        self.driver.find_element_by_xpath('//*[@text="保存后自动发送邀请通知"]').click()
        self.driver.find_element_by_xpath('//*[@text="保存"]').click()

        # pass
