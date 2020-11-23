import time
import logging
from Library.BasePage import BasePage

class JavaAlert(BasePage):



    def __init__(self, driver):
        self.driver = driver
        super.__init__(driver)

    def java_alert(self):
        self.driver.get('http://localhost:7080/javascript_alerts')
        self.driver.find_element_by_xpath("//*[@id=\'content\']/div/ul/li[1]/button").click()
        alert = self.driver.switch_to.alert.text
        assert alert, "I am a JS Alert"
        self.driver.switch_to.alert.accept()
        time.sleep(2)

        # Confirm button
        self.driver.find_element_by_xpath("//*[@id=\'content\']/div/ul/li[2]/button").click()
        confirm = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        assert confirm, "I am a JS Confirm"
        time.sleep(2)

        # JS Prompt Button
        self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/ul/li[3]/button").click()
        time.sleep(2)
        self.driver.switch_to.alert.send_keys('I love Ocean city')
        time.sleep(2)
        data = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        result_txt = self.driver.find_element_by_css_selector("#result")
        assert result_txt.text[13:], 'I love Ocean city'
        logging.info('Your Text is ' + result_txt.text[13:])