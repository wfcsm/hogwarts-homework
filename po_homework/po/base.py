from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver_base: WebDriver = None):
        if driver_base == None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(executable_path='../../driver/chromedriver',
                                           options=opt)

            self.driver.implicitly_wait(5)
        else:
            self.driver = driver_base

    def find_and_click(self, locator):
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
        self.driver.find_element(*locator).click()
