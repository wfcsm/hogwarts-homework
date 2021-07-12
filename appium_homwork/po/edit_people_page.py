from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from appium_homwork.po.base_page import BasePage


class EditPeoplePage(BasePage):
    _NAME=(MobileBy.XPATH,'//*[contains(@text,"姓名")]/../android.widget.EditText')
    _PHONE_NUMBER = (MobileBy.XPATH,'//*[contains(@text,"手机")]/../android.widget.EditText')
    _SET_DEPARTMENT = (MobileBy.XPATH,'//*[@text="设置部门"]')
    _SURE=(MobileBy.XPATH,'//*[contains(@text,"确定")]')
    _TOGGLE_SEND_INVITATION=(MobileBy.XPATH,'//*[@text="保存后自动发送邀请通知"]')
    _SUBMIT=(MobileBy.XPATH,'//*[@text="保存"]')

    def edit_people(self):
        from appium_homwork.po.add_people_page import AddPeoplePage
        self.find_and_sendkey(*self._NAME,'asd')
        self.find_and_sendkey(*self._PHONE_NUMBER,'13429651922')
        self.find_and_click(*self._SET_DEPARTMENT)
        self.find_and_click(*self._SURE)
        self.find_and_click(*self._TOGGLE_SEND_INVITATION)
        self.find_and_click(*self._SUBMIT)
        # self.driver.find_element_by_xpath('//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys('xcv')
        # self.driver.find_element_by_xpath('//*[contains(@text,"手机")]/../android.widget.EditText').send_keys('13429651915')
        # self.driver.find_element_by_xpath('//*[@text="设置部门"]').click()
        # self.driver.find_element_by_xpath('//*[contains(@text,"确定")]').click()
        # 取消自动发送邀请
        # self.driver.find_element_by_xpath('//*[@text="保存后自动发送邀请通知"]').click()
        # self.driver.find_element_by_xpath('//*[@text="保存"]').click()

        return AddPeoplePage(self.driver)