from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multipledispatch import dispatch



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def clicker(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return elem.text

    def is_visible(self, by_locator):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(elem)

    def isnot_visible(self, by_locator):
        elem = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        return bool(elem)

    def is_selected(self, by_locator):
        elem = WebDriverWait(self.driver, 10).until(EC.element_located_to_be_selected(by_locator))
        return bool(elem)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_url(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_matches(url))
        return self.driver.current_url

    def drag_drop(self, s_element, d_element):
        ActionChains(self.driver).drag_and_drop(s_element, d_element).perform()

    def is_checked(self, driver, item):
        checked = driver.execute_script(("return document.getElementById('%s').checked") % item)
        return checked

    def drop_down(self, element, index):
        Select(element).select_by_index(index)

    def javaScript_click(self, driver, elem):
        driver.execute_script('arguments[0].click();', elem)

    def scrollView(self, driver, elem):
        driver.execute_script('arguments[0].ScrollIntoView(true)', elem)

    def scrollPixel(self, driver):
        self.driver.execute_script("window.scrollBy(0, -10);")
