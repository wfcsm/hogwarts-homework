from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_and_click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def find_and_sendkey(self,by,locator,key):
        self.driver.find_element(by, locator).send_keys(key)