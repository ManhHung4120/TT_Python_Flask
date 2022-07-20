from loginDAO.login_method import check
import pytest


DATA = [
    (1,  "hung", "1235", None),
    (2,  "hung", "1234", True),
]


@pytest.mark.parametrize("case,username_test,password_test,expect", DATA)
def test_check(case, username_test, password_test, expect):
    assert check(username_test, password_test) == expect
