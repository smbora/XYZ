from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from .common import CommonOps



class depositWithdraw(CommonOps):
    
    DEPOSIT_BTN_LOCATOR = (By.XPATH, "//button[@class='btn btn-lg btn-primary' and starts-with(@ng-click, 'deposit()')]")
    
    def click_deposit(self):
        self.find(self.DEPOSIT_BTN_LOCATOR).click()