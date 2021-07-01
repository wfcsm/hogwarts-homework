import allure
import pytest


@allure.feature('计算器')
class TestCalculator:
    # 加法
    @allure.title('相加功能title')
    @allure.story('相加功能story')
    @pytest.mark.add
    def test_add(self, get_calc_object,get_datas):
        assert get_datas[2] == get_calc_object.add(get_datas[0],get_datas[1])

    # 除法
    @pytest.mark.div
    def test_div(self, get_calc_object,get_datas):
        assert get_datas[2] == get_calc_object.div(get_datas[0], get_datas[1])

