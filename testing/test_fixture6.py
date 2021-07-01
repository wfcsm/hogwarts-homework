import pytest


@pytest.fixture(params=['tom','jerry','linda'],
                ids=['name1','name2','name3'])
def login(request):
    myparam = request.param
    print(f"用户名：{request.param}")
    yield myparam
    print("登录")


def test_case1(login):
    print(login)
