import time

from Library.BasePage import BasePage
from Library.Locators import Locator

class DynamicControls(BasePage):

    url_dynamicControl = Locator.url_dynamicControl
    add_btn = Locator.add_btn
    add_msg = Locator.add_msg
    remove_btn = Locator.remove_btn
    enable_btn = Locator.enable_btn
    enable_txt = Locator.enable_txt
    disable_btn = Locator.disable_btn
    disable_msg = Locator.disable_msg

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def dynamicContents(self):
        self.driver.get(self.url_dynamicControl)
        self.click(self.add_btn)
        self.isnot_visible(self.add_msg)
        self.driver.find_element_by_xpath(self.remove_btn).click()
        self.is_visible(self.enable_btn)
        time.sleep(4)

        self.click(self.disable_btn)
        assert self.driver.find_element_by_xpath(self.enable_txt).text, "It's enabled!"
        self.click(self.disable_btn)
        assert self.driver.find_element_by_xpath(self.disable_msg).text, "It's disabled!"
