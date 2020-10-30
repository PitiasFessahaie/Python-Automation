from Library.BasePage import BasePage
import logging
from Library.Locators import Locator

class Login_fail(BasePage):
    username = Locator.username1
    password = Locator.password1
    login = Locator.login
    login_url = Locator.login_url

    def __init__(self, driver):
        self.driver = driver

    def test_login_fail(self, username, password):
        self.driver.get(self.login_url)
        logging.info('adding username and password')
        self.send_keys(self.username, username)
        self.send_keys(self.username, username)
        logging.info('clicking the submit button')
        self.click(self.login)

