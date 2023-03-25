from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


class TestSample():

    @pytest.fixture()
    def setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed")
        #


    def test_login(self, setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(by=By.NAME, value="username").clear()
        driver.find_element(by=By.NAME, value="username").send_keys("Admin")
        driver.find_element(by=By.NAME, value="password").clear()
        driver.find_element(by=By.NAME, value="password").send_keys("admin123")
        driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        title_obtained = driver.title
        assert title_obtained == "OrangeHRM"
        time.sleep(2)

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("test completed")