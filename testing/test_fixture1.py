import pytest


@pytest.fixture()
def login():
    print("登录")
    return 'token'


@pytest.fixture()
def connectDBA():
    print("连接数据库")
    return "database_datas"


def test_case1(login,connectDBA):
    # 登录
    # 连接数据库
    print(f"登录操作的返回数据：{login}")
    print(f"连接数据库的返回数据{connectDBA}")
    print("case1")

@pytest.mark.usefixtures('login')
def test_case2():
    print("case2")

def test_case3(login):
    # 登录
    print("case3")