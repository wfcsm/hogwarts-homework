from selenium.webdriver.common.by import By

from testing.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element(By.ID, 'draggable').text)
        print(self.driver.switch_to.parent_frame())
        self.driver.switch_to_default_content()
        print(self.driver.find_element(By.ID, 'submitBTN').text)


