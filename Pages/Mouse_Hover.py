import time

from selenium.webdriver import ActionChains


class MouseHover:

    url_MouseHover = 'http://localhost:7080/hovers'

    def __init__(self, driver):
        self.driver = driver

    def mouseHover(self):
        self.driver.get(self.url_MouseHover)
        user1 = self.driver.find_element_by_xpath("//*[@id=\'content\']/div/div[1]/img")
        user2 = self.driver.find_element_by_xpath("//*[@id=\'content\']/div/div[2]/img")
        user3 = self.driver.find_element_by_xpath("//*[@id=\'content\']/div/div[3]/img")
        user1info = self.driver.find_element_by_xpath("//*[@id=\'content\']/div/div[1]/div/h5")
        user2info = self.driver.find_element_by_xpath("//*[@id=\'content\']/div/div[2]/div/h5")
        user3info = self.driver.find_element_by_xpath("//*[@id=\'content\']/div/div[3]/div/h5")

        ActionChains(self.driver).move_to_element(user1).perform()
        assert user1info.text, 'name: user1'
        time.sleep(2)
        ActionChains(self.driver).move_to_element(user2).perform()
        assert user2info.text, 'name: user2'
        time.sleep(2)
        ActionChains(self.driver).move_to_element(user3).perform()
        assert user3info.text, 'name: user3'
        time.sleep(2)