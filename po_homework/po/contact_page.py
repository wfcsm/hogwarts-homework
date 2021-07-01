import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from po_homework.po.base import Base


class ContactPage(Base):
    _ADD_BUTTON = (By.CSS_SELECTOR, 'a>.member_colLeft_top_addBtn')
    _CREATE_DEPARTMENT = (By.CSS_SELECTOR, '.js_create_party')
    _DEPARTMENT_NAME = (By.CSS_SELECTOR, '.inputDlg_item>input')
    _AFFILIATION_LIST=(By.CSS_SELECTOR, '.js_toggle_party_list')
    _AFFILIATION = (By.XPATH, '//a[text()="未命名企业"]')
    _SURE=(By.XPATH, '//a[text()="确定"]')

    def click_add_button(self):
        self.find_and_click(self._ADD_BUTTON)

    def add_department(self):
        self.find_and_click(self._CREATE_DEPARTMENT)

        department = self.driver.find_elements(*self._DEPARTMENT_NAME)
        department[0].send_keys('测试1')

        # self.driver.find_element(*self._AFFILIATION_LIST).click()
        self.find_and_click(self._AFFILIATION_LIST)

        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self._AFFILIATION))
        affiliation_department=self.driver.find_elements(*self._AFFILIATION)
        affiliation_department[-1].click()
        self.find_and_click(self._SURE)

    def get_department(self):
        target=self.driver.find_element(By.XPATH, '//a[text()="测试1"]').text

        return target
