import pytest


@pytest.fixture()
def get_ini(pytestconfig):
    marks = pytestconfig.getini('markers')
    log_cli = pytestconfig.getini('log_cli')
    print(marks,log_cli)


def test_pytestconfig(get_ini):
    pass