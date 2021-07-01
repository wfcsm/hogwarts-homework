import pytest


@pytest.fixture()
def login():
    print("登录")
    yield 'token'
    print("登出")


def test_case1(login):
    pass
    # print(login)
    # print("case1")


def test_case2():
    pass
    # print("case2")


def test_case3():
    pass
    # print("case3")