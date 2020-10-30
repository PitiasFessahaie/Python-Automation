import time


class Dynamic_Content:

    dynamic_url = 'http://localhost:7080/dynamic_content'

    def __init__(self, driver):
        self.driver = driver


    def test_dynamicContent(self):
        self.driver.get(self.dynamic_url)
        for x in range(2):
            self.driver.refresh()
            time.sleep(2)
            links = []
            elems = self.driver.find_elements_by_tag_name('img')
            for elem in elems:
                links.append(elem.get_attribute('src'))
        return links
