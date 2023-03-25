from selenium import webdriver
import time
import HtmlTestRunner

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))


from sample_tests.pages.login_page import LoginPage
from sample_tests.pages.home_page import HomePage


import unittest


class Logintests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home = HomePage(driver)
        home.click_welcome_link()
        time.sleep(2)
        home.click_logout_link()


        # driver.find_element(by=By.NAME, value="username").send_keys("Admin")
        # driver.find_element(by=By.NAME, value="password").send_keys("admin123")
        # driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        # driver.find_element(by=By.XPATH, value="//img[@class='oxd-userdropdown-img']").click()
        # driver.find_element(by=By.LINK_TEXT, value="Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("test completed")



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../report"))



