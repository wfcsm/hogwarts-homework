import pytest


@pytest.fixture(scope='module')
def other():
    print("other")


@pytest.fixture(scope='module')
def login():
    print("登录")
    return 'token'


def test_case1(login):
    print("case1")


def test_case2(login):
    print("case2")


def test_case3(login):
    print("case3")