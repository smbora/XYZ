from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from .common import CommonOps

class Login(CommonOps):

    CUSTOMER_LOGIN_BTN_LOCATOR = (By.XPATH, "//button[@class='btn btn-primary btn-lg' and starts-with(@ng-click, 'customer()')]")
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
        
    def check_loged_user(self,username):
        try:
            self.wait_for((By.XPATH, f"//span[text()='{username}']"))
            return("login success")
        except TimeoutException:
            return("login fail")
