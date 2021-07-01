import pytest


@pytest.mark.parametrize('name',['赫敏','哈利波特'])
def test_hook(name):
    print(f'姓名：{name}')


def test_aaa():
    print('testaaaaaaa')