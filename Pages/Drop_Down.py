from selenium.webdriver.support.select import Select
from Library.Locators import Locator
from Library.BasePage import BasePage
import time
import logging


class Drop_Down(BasePage):
    dropDown_url = Locator.dropDown_url
    dropdown1 = Locator.dropDown_btn

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def dropDown(self):

        self.driver.get(self.dropDown_url)
        drop = self.driver.find_element_by_css_selector(self.dropdown1)
        # Select(drop).select_by_index(1)
        self.drop_down(drop, 1)
        assert Select(drop).first_selected_option.text, 'Option 1'
        logging.info('Assertion Pass Option 1')
        time.sleep(2)
        #Select(drop).select_by_index(2)
        self.drop_down(drop, 2)
        assert Select(drop).first_selected_option.text, 'Option 2'
        logging.info('Assertion Pass Option 2')

