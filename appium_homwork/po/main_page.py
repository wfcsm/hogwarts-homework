from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


from appium_homwork.po.base_page import BasePage
from appium_homwork.po.contacts_page import ContactsPage


class MainPage(BasePage):
    _CONTACT=(MobileBy.XPATH,'//*[@text="通讯录"]')

    def go_to_contacts_page(self):
        self.find_and_click(*self._CONTACT)
        # self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        return ContactsPage(self.driver)
        # pass
