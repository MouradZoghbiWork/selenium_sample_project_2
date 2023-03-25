from selenium.webdriver.common.by import By
from sample_tests.locators.locators import Locators

class HomePage:

    def __init__(self,driver):
        self.driver = driver
        self.welcome_link_xpath = Locators.welcome_link_xpath
        self.logout_partial_link_text = Locators.logout_partial_link_text

    def click_welcome_link(self):
        self.driver.find_element(by=By.XPATH, value=self.welcome_link_xpath).click()

    def click_logout_link(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.logout_partial_link_text).click()
