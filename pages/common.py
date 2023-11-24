from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains



class CommonOps:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 5)
        self._action = ActionChains(self.driver)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))
    
    def wait_for_clickable(self, locator):
        return self._wait.until((ec.element_to_be_clickable(locator)))

    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def context_click(self, element):
        return self._action.context_click(element)

    def alert(self):
        return self._wait.until(ec.alert_is_present())