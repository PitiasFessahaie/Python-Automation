import time


class Notification_Message:
    def __init__(self, driver):
        self.driver = driver

    def notification_msg(self):
        self.driver.get('http://localhost:7080/notification_message_rendered')
        lst = []

        for i in range(3):
            self.driver.find_element_by_link_text('Click here').click()
            time.sleep(2)
            lst.append(self.driver.find_element_by_css_selector('.flash.notice').text)
        l = [a[:-2] for a in lst]
        if 'Action successful' in l:
            assert True
        else:
            assert False