from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from appium_homwork.po.add_people_page import AddPeoplePage
from appium_homwork.po.base_page import BasePage


class ContactsPage(BasePage):
    _ADD_MEMBER=(MobileBy.XPATH,'//*[@text="添加成员"]')
    def go_to_add_people_page(self):
        self.find_and_click(*self._ADD_MEMBER)
        # self.driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        return AddPeoplePage(self.driver)

