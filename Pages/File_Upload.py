
class File_Upload:
    file = '/Users/pitiasfessahaie/Downloads/some-file.txt'
    url_fileUpload = 'http://localhost:7080/upload'
    attach_btn = '#file-upload'
    submit_btn = '#file-submit'

    def __init__(self, driver):
        self.driver = driver

    def fileUpload(self):
        self.driver.get(self.url_fileUpload)
        self.driver.find_element_by_css_selector(self.attach_btn).send_keys(self.file)
        self.driver.find_element_by_css_selector(self.submit_btn).click()
        assert self.driver.find_element_by_tag_name('h3').text, 'File Uploaded!'

