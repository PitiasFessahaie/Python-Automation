import logging

from selenium.common.exceptions import WebDriverException


class Java_ScriptError:

    def __init__(self, driver):
        self.driver = driver

    def java_scriptError(self):
        self.driver.get("http://localhost:7080/javascript_error")

        error = self.check_browser_errors(self.driver)
        assert error[0]['message'][44:], "Uncaught TypeError: Cannot read property 'xyz' of undefined"

    def check_browser_errors(self, driver):

        try:
            browserlogs = driver.get_log('browser')
        except (ValueError, WebDriverException) as e:
            logging.error(f'cant get the error in {driver} due to Error: {e}')
            return []

        errors = []
        for entry in browserlogs:
            if entry['level'] == 'SEVERE':
                errors.append(entry)
        return errors
