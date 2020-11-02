from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from Library.Locators import Locator
from Library.BasePage import BasePage


class DragDrop(BasePage):

    url = Locator.dd_url
    Abox = Locator.Abox
    Bbox = Locator.Bbox


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def Drag_Drop(self):
        self.driver.get(self.url)
        boxa = self.driver.find_element_by_css_selector(self.Abox)
        boxb = self.driver.find_element_by_css_selector(self.Bbox)
        self.drag_drop(boxa, boxb)



