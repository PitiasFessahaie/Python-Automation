from selenium import webdriver
from selenium.webdriver.support.select import Select
from Pages.Dynamic_Content import Dynamic_Content
from Pages.Login_Success import Login_Success
from Pages.Login_Failure import Login_fail
from Pages.Check_Box import Check_Box
from Pages.Context_Menu import Context_Menu
from Pages.Drag_and_Drop import DragDrop
from Pages.Drop_Down import Drop_Down
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
        lp = Login_Success(self.driver)
        lp.test_login(self.username, self.password)
        time.sleep(3)
        self.assertEqual(self.driver.current_url, self.success_url)

    def test_LoginFailure(self):
        lf = Login_fail(self.driver)
        lf.test_login_fail(self.username, 'password!')
        time.sleep(3)
        self.assertNotEqual(self.driver.current_url, self.success_url)

    def test_Checkbox(self):
        ch = Check_Box(self.driver)
        ch.test_checkBox()
        time.sleep(3)

    def test_ContextMenu(self):
        cm = Context_Menu(self.driver)
        cm.ContextMenu()
        time.sleep(3)
        self.assertEqual(self.driver.switch_to.alert.text, 'You selected a context menu')
        self.driver.switch_to.alert.accept()

    def test_Drag_Drop(self):
        dd = DragDrop(self.driver)
        dd.Drag_Drop()
        time.sleep(3)
        if self.driver.find_element_by_css_selector('#column-b').text == 'A':
            print('The Box dragged Successfully')
        else:
            print('The Box is not dragged Successful')

    def test_DropDown(self):
        dd = Drop_Down(self.driver)
        dd.dropDown()
        time.sleep(2)

    def test_dynamicContent(self):
        dc = Dynamic_Content(self.driver)
        list1 = dc.test_dynamicContent()
        list2 = dc.test_dynamicContent()
        # print(list1)
        # print(list2)
        self.assertNotEqual(list1, list2)







if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='/Users/pitiasfessahaie/Documents/Pycharm/Python-Automation/Report'))