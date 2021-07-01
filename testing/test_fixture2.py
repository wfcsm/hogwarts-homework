import pytest


@pytest.fixture()
def login():
    print("登录")
    return 'token'

@pytest.mark.parametrize("a,b",[
    [1,2],
    [3,4]
])
def test_params(login,a,b):
    print(a,b,login)
