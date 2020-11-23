import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Library.Locators import Locator


class FloatingFile:
    url_FloatingFile = Locator.url_FloatingFile
    scroll_elem = Locator.scroll_elem

    def __init__(self, driver):
        self.driver = driver

    def floating_file(self):
        self.driver.get(self.url_FloatingFile)
        elem = self.driver.find_element_by_xpath(self.scroll_elem)
        self.driver.execute_script("window.scrollBy(0, 3000);")
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.scroll_elem)))

