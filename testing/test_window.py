from selenium.webdriver.common.by import By

from testing.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element(By.LINK_TEXT,'登录').click()
        print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT,'立即注册').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        print(self.driver.current_window_handle)
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__userName').send_keys('username')
        pass