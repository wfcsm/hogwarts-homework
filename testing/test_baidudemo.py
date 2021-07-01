import time

import allure
import pytest
from selenium import webdriver


@allure.testcase(url='https://www.baidu.com',name='百度')
@allure.feature('百度搜索')
@pytest.mark.parametrize('test_data1',['allure', 'pytest', 'unittest'])
def test_step_demo(test_data1):
    with allure.step('打开百度网页'):
        driver=webdriver.Chrome(executable_path='./driver/chromedriver')
        driver.get('https://www.baidu.com')
        driver.maximize_window()

    with allure.step(f'输入关键词{test_data1}'):
        driver.find_element_by_id('kw').send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id('su').click()
        time.sleep(2)

    with allure.step('保存图片'):
        current=str(time.time())
        driver.save_screenshot(filename=f'./datas/{current}.png')
        allure.attach.file(source=f'./datas/{current}.png',
                           name=current,
                           attachment_type=allure.attachment_type.PNG)

    with allure.step('关闭浏览器'):
        driver.quit()