import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class FloatingFile:
    def __init__(self, driver):
        self.driver = driver

    def floating_file(self):
        self.driver.get('http://localhost:7080/floating_menu')
        elem = self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[2]/a')
        self.driver.execute_script("window.scrollBy(0, 3000);")
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menu"]/ul/li[2]/a')))

