import logging
from Library.Locators import Locator
from selenium.webdriver import ActionChains


class Context_Menu:

    context_url = Locator.context_url
    right_click = Locator.right_click

    def __init__(self, driver):
        self.driver = driver

    def ContextMenu(self):

        self.driver.get(self.context_url)
        rc = self.driver.find_element_by_css_selector(self.right_click)
        ActionChains(self.driver).context_click(rc).perform()



