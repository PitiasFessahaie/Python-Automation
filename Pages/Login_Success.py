import logging


class Login_Success:

    username = '#username'
    password = '#password'
    login = '.radius'
    login_url = 'http://localhost:7080/login'

    def __init__(self, driver):
        self.driver = driver

    def test_login(self, username, password):
        self.driver.get(self.login_url)
        logging.info('adding username and password')
        self.driver.find_element_by_css_selector(self.username).send_keys(username)
        self.driver.find_element_by_css_selector(self.password).send_keys(password)
        logging.info('clicking the submit button')
        self.driver.find_element_by_css_selector(self.login).click()

