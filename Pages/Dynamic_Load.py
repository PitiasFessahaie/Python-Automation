from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Library.Locators import Locator
class Dynamic_Load:

    url_dynamic_load = Locator.url_dynamic_load

    def __init__(self, driver):
        self.driver = driver

    def dynamic_load(self):
        self.driver.get(self.url_dynamic_load)
        self.driver.find_element_by_xpath('//*[@id="start"]/button').click()
        texter = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#finish'))).text
        assert texter, 'Hello World!'
