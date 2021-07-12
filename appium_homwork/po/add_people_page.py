from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from appium_homwork.po.base_page import BasePage


class AddPeoplePage(BasePage):
    _INPUT=(MobileBy.XPATH,'//*[contains(@text,"手动输入添加")]')

    def go_to_edit_people_page(self):
        from appium_homwork.po.edit_people_page import EditPeoplePage
        self.find_and_click(*self._INPUT)
        # self.driver.find_element_by_xpath('//*[contains(@text,"手动输入添加")]').click()

        return EditPeoplePage(self.driver)