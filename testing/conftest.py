from typing import List

import pytest
import yaml

from pythoncode.calculator import Calculator


@pytest.fixture(scope="class")
def get_calc_object():
    print("计算开始")
    calc=Calculator()
    yield calc
    print("计算结束")


# 获取 测试数据
def get_calc_data(data_url):
    with open(file=data_url) as f:
        totals = yaml.safe_load(f)
    return (totals['datas'], totals['ids'])



# # 测试 获取数据的方法
# def test_getdatas():
#     print(get_calc_data())


@pytest.fixture(params=get_calc_data(data_url='./datas/calc.yml')[0],
                ids=get_calc_data(data_url='./datas/calc.yml')[1])
def get_datas(request):
    return request.param





def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
        if 'hook' in item.name:
            item.add_marker(pytest.mark.hook)
        if 'aaa' in item.name:
            item.add_marker(pytest.mark.aaa)

