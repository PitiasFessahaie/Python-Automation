import logging
from Library.Locators import Locator
from Library.BasePage import BasePage


class Check_Box(BasePage):
    checkbox_url = Locator.checkbox_url
    checkbox1 = Locator.checkbox1
    checkbox2 = Locator.checkbox2

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


    def checkBox(self):
        self.driver.get(self.checkbox_url)
        ch1 = self.driver.find_element_by_xpath(self.checkbox1)
        ch2 = self.driver.find_element_by_xpath(self.checkbox2)
        if ch1.is_selected():
            print('checkbox 1 is already selected')
            logging.info('Checking if ch1 is clicked')
        else:
            self.clicker(ch1)
            print('check box 1 is clicked')

        if ch2.is_selected():
            print('checkbox2 is already selected')
            logging.info('Checking if ch2 is clicked')
        else:
            self.clicker(ch2)
            print('check box is clicked')
        