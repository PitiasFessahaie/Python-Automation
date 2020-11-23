from Library.Locators import Locator

class File_Upload:

    file_name = Locator.file_name
    url_fileUpload = Locator.url_fileUpload
    attach_btn = Locator.attach_btn
    submit_btn = Locator.submit_btn

    def __init__(self, driver):
        self.driver = driver

    def fileUpload(self):
        self.driver.get(self.url_fileUpload)
        self.driver.find_element_by_css_selector(self.attach_btn).send_keys(self.file_name)
        self.driver.find_element_by_css_selector(self.submit_btn).click()
        assert self.driver.find_element_by_tag_name('h3').text, 'File Uploaded!'

