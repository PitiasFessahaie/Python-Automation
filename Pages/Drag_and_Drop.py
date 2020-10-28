from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class DragDrop:
    url = 'http://localhost:7080/drag_and_drop'
    Abox = '#column-a'
    Bbox = '#column-b'

    def __init__(self, driver):
        self.driver = driver

    def Drag_Drop(self):
        self.driver.get(self.url)
        boxa = self.driver.find_element_by_css_selector(self.Abox)
        boxb = self.driver.find_element_by_css_selector(self.Bbox)
        ActionChains(self.driver).drag_and_drop(boxa, boxb).perform()



