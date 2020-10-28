from selenium import webdriver
from Pages.Login_Success import Login_Success
from Pages.Login_Failure import Login_fail
import unittest
import logging
import time
from pyunitreport import HTMLTestRunner


class SmokeTest(unittest.TestCase):
    username = 'tomsmith'
    password = 'SuperSecretPassword!'
    success_url = 'http://localhost:7080/secure'
    logging.basicConfig(filename='/Users/pitiasfessahaie/Documents/Pycharm/Python-Automation/Library/test.log', format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(
            executable_path='/Users/pitiasfessahaie/Documents/Pycharm/Python-Automation/drivers/chromedriver')

        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.set_page_load_timeout(10)
        cls.driver.delete_all_cookies()

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_LoginSuccess(self):
        driver = self.driver
        lp = Login_Success(driver)
        lp.test_login(self.username, self.password)
        time.sleep(3)
        self.assertEqual(driver.current_url, self.success_url)

    def test_LoginFailure(self):
        driver = self.driver
        lf = Login_fail(driver)
        lf.test_login_fail(self.username, 'password!')
        time.sleep(3)
        self.assertNotEqual(driver.current_url, self.success_url)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='/Users/pitiasfessahaie/Documents/Pycharm/Python-Automation/Report'))