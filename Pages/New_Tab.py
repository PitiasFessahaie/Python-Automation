import time

class NewTab:
    def __init__(self, driver):
        self.driver = driver

    def new_Tab(self):
        self.driver.get('http://localhost:7080/windows')
        btn = self.driver.find_element_by_link_text("Click Here").click()
        time.sleep(2)
        all = self.driver.window_handles
        for a in all:
            self.driver.switch_to.window(a)
        assert self.driver.find_element_by_tag_name('h3').text, 'New Window'
        time.sleep(2)