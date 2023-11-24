import pytest
from pages.login import Login
from pages.depositWithdraw import depositWithdraw


@pytest.fixture
def login(driver):
    login = Login(driver)
    login.customer_login()
    login.select_user(username)
    login.click_login_button()

    return login

username = "Hermoine Granger"

@pytest.mark.parametrize('login', [username], indirect=True)
class TestAll:

    def test_user_login(driver, login):
        wrong_username = "Harry Potter"

        assert login.check_loged_user(username) == "login success"
        assert login.check_loged_user(wrong_username) == "login fail"

    def test_deposit(driver, login):
        deposit = depositWithdraw(login)
