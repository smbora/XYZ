from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from .common import CommonOps

class userPage(CommonOps):

## Login helpers
    CUSTOMER_LOGIN_BTN_LOCATOR = (By.XPATH, "//button[contains(@ng-click,'customer()')]")
    MANAGER_LOGIN_BTN_LOCATOR = (By.XPATH, "//button[normalize-space()='Bank Manager Login']")
    LOGIN_BTN_LOCATOR = (By.XPATH, "//button[normalize-space()='Login']")
    USER_SELECT = (By.ID, "userSelect")
    
    def customer_login(self):
        self.wait_for_clickable(self.CUSTOMER_LOGIN_BTN_LOCATOR).click()

    def manager_login(self):
        self.wait_for_clickable(self.MANAGER_LOGIN_BTN_LOCATOR).click()

    def select_user(self, username):
        user_select = Select(self.wait_for(self.USER_SELECT))
        user_select.select_by_visible_text(username)

    def click_login_button(self):
        self.wait_for(self.LOGIN_BTN_LOCATOR).click()
        
    def check_loged_user(self, username):
        try:
            self.wait_for((By.XPATH, f"//span[text()='{username}']"))
            return("login success")
        except TimeoutException:
            return("login fail")
## Balance helpers
    ACCOUNT_SUMARY_SELECTOR = "//div[contains(@ng-hide,'noAccount') and contains(.,'Account Number :') and contains(.,'Balance :') and contains(.,'Currency :')]"
    BALANCE_LOCATOR = (By.XPATH, f"{ACCOUNT_SUMARY_SELECTOR}/child::strong[2]")
    def get_balance(self):
        return self.wait_for(self.BALANCE_LOCATOR).text

## Deposit and withdraw helpers
    DEPOSIT_BTN_LOCATOR = (By.XPATH, "//button[contains(@ng-click,'deposit()')]")
    DEPOSIT_SUBMIT_LOCATOR = (By.XPATH, "//form[contains(@ng-submit,'deposit()')]/button[@type='submit']")
    AMOUNT_INPUT_LOCATOR = (By.XPATH, "//input[contains(@ng-model,'amount')]")
    MESSAGE_LOCATOR = (By.XPATH, "//span[contains(@class,'ng-binding') and contains(@class,'error')]")
    
    def select_deposit(self):
        self.wait_for_clickable(self.DEPOSIT_BTN_LOCATOR).click()

    def set_amount(self, value):
        self.wait_for(self.AMOUNT_INPUT_LOCATOR).send_keys(value)

    def click_deposit(self):
        self.wait_for_clickable(self.DEPOSIT_SUBMIT_LOCATOR).click()

    def get_message(self):
        try:
            value = self.wait_for(self.MESSAGE_LOCATOR).text
            return(value)
        except TimeoutException:
            return("No message")
