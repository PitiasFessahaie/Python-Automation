import logging
from Library.Locators import Locator
from Library.BasePage import BasePage


class Login_Success(BasePage):
    username = Locator.username
    password = Locator.password
    login = Locator.login
    login_url = Locator.login_url

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def test_login(self, username, password):
        self.driver.get(self.login_url)
        logging.info('adding username and password')
        self.send_keys(self.username, username)
        self.send_keys(self.password, password)
        logging.info('clicking the submit button')
        self.click(self.login)
