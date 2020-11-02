import os
import time
from Library.Locators import Locator

class File_Download:
    file_path = Locator.file_path
    url_Filedownload = Locator.url_Filedownload
    file = Locator.file

    def __init__(self, driver):
        self.driver = driver

    def File_Download(self):
        self.driver.get(self.url_Filedownload)
        self.driver.find_element_by_xpath(self.file).click()
        while not os.path.exists(self.file_path):
            time.sleep(1)
        if os.path.isfile(self.file_path):
            assert True
            print(f'File {self.file_path} downloaded Successful !!!')
        else:
            raise ValueError(f'The file {self.file_path} doesnt Exits')
