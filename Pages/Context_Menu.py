import logging
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver import ActionChains


class Context_Menu:

    context_url = 'http://localhost:7080/context_menu'
    right_click = '#hot-spot'

    def __init__(self, driver):
        self.driver = driver

    def ContextMenu(self):

        self.driver.get(self.context_url)
        rc = self.driver.find_element_by_css_selector(self.right_click)
        ActionChains(self.driver).context_click(rc).perform()



