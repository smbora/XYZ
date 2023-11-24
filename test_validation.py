import pytest
from pages.userPage import userPage

username = "Hermoine Granger"

class TestAll:
    @pytest.fixture
    def login(self, driver):
        login = userPage(driver)
        login.customer_login()
        login.select_user(username)
        login.click_login_button()

        return login

    @pytest.mark.parametrize('login', [username], indirect=True)
    def test_user_login(driver, login):
        wrong_username = "Harry Potter"

        assert login.check_loged_user(username) == "login success"
        assert login.check_loged_user(wrong_username) == "login fail"

    @pytest.mark.parametrize('login', [username], indirect=True)
    def test_deposit(driver, login):
        balance = login.get_balance()
        amount = 10
        login.select_deposit()
        login.set_amount(amount)
        login.click_deposit()

        assert int(login.get_balance()) == int(balance) + int(amount)
        assert login.get_message() == "Deposit Successful"
