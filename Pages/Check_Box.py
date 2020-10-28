import logging

import time


class Check_Box:
    checkbox_url = 'http://localhost:7080/checkboxes'
    checkbox1 = '//body//input[1]'
    checkbox2 = '//body//input[2]'

    def __init__(self, driver):
        self.driver = driver

    # def is_checked(self, driver, item):
    #     checked = driver.execute_script(("return document.getElementById('%s').checked") % item)
    #     return checked

    def test_checkBox(self):
        self.driver.get(self.checkbox_url)
        ch1 = self.driver.find_element_by_xpath(self.checkbox1)
        ch2 = self.driver.find_element_by_xpath(self.checkbox2)
        if ch1.is_selected():
            print('checkbox 1 is selected')
            logging.info('Checking if ch1 is clicked')
        else:
            print('check box 1 is clicked')
            ch1.click()

        if ch2.is_selected():
            print('checkbox2 is selected')
            logging.info('Checking if ch2 is clicked')
        else:
            ch2.click()
            print('check box is clicked')
        