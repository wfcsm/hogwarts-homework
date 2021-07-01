import os

from selenium import webdriver


class Base:
    def setup(self):
        b=os.getenv('b')
        if b == 'chrmoe':
            self.driver = webdriver.Chrome(executable_path='./driver/chromedriver')
        elif b == 'safari':
            self.driver = webdriver.Safari()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()