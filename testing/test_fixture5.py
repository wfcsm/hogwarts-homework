
import pytest
import yaml


from pythoncode.calculator import Calculator


# 获取 测试数据
def get_calc_data(data_url):
    with open(file=data_url) as f:
        totals = yaml.safe_load(f)
    return (totals['datas'], totals['ids'])


# 测试 获取数据的方法
def test_getdatas():
    print(get_calc_data())

@pytest.fixture(scope="class")
def get_calc_object():
    print("计算开始")
    calc=Calculator()
    yield calc
    print("计算结束")

class TestCalculator:
    # 加法
    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect', get_calc_data(data_url='./datas/calc.yml')[0],
                             ids=get_calc_data(data_url='./datas/calc.yml')[1])
    def test_add(self, a, b, expect,get_calc_object):
        # calc = Calculator()
        assert expect == get_calc_object.add(a,b)

    # 除法
    @pytest.mark.div
    @pytest.mark.parametrize("a,b,expect", argvalues=get_calc_data(data_url='./datas/calc_div.yml')[0],
                             ids=get_calc_data(data_url='./datas/calc_div.yml')[1])
    def test_div(self, a, b, expect,get_calc_object):
        assert expect == get_calc_object.div(a, b)

    # 减法
    @pytest.mark.parametrize("a,b,expect",argvalues=get_calc_data(data_url='./datas/calc_sub.yml')[0],
                             ids=get_calc_data(data_url='./datas/calc_sub.yml')[1])
    def test_sub(self,a,b,expect,get_calc_object):
        assert expect == get_calc_object.sub(a,b)


    # 乘法
    @pytest.mark.parametrize("a,b,expect",argvalues=get_calc_data(data_url='./datas/calc_mul.yml')[0],
                             ids=get_calc_data(data_url='./datas/calc_mul.yml')[1])
    def test_mul(self,a,b,expect,get_calc_object):
        assert expect == get_calc_object.mul(a,b)
