import time


class IFRAME:
    url_iframe = 'http://localhost:7080/iframe'
    text_field ='#tinymce'

    def __init__(self, driver):
        self.driver = driver

    def iframe(self):
        self.driver.get(self.url_iframe)
        self.driver.switch_to.frame(0)
        text_field = self.driver.find_element_by_css_selector(self.text_field)
        text_field.clear()
        text_field.send_keys('I love USA!')
        time.sleep(2)
        data = text_field.text
        assert data, 'I love USA!'