from selenium import webdriver
from selenium.webdriver.common.by import By

from po_homework.po.base import Base
from po_homework.po.contact_page import ContactPage


class MainPage(Base):
    _CONTACTS=(By.ID, 'menu_contacts')

    def go_to_contact(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(executable_path='../../driver/chromedriver',
        #                                options=opt)
        self.driver.get(url='https://work.weixin.qq.com/wework_admin/frame')
        # self.driver.implicitly_wait(5)
        self.driver.find_element(*self._CONTACTS).click()

        return ContactPage(self.driver)
