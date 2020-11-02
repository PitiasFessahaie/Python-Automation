import os
import time


class File_Download:
    file_path = '/Users/pitiasfessahaie/Downloads/some-file.txt'

    def __init__(self, driver):
        self.driver = driver

    def File_Download(self):
        self.driver.get('http://localhost:7080/download')
        self.driver.find_element_by_xpath('//*[@id="content"]/div/a[1]').click()
        while not os.path.exists(self.file_path):
            time.sleep(1)
        if os.path.isfile(self.file_path):
            assert True
            print(f'File {self.file_path} downloaded Successful !!!')
        else:
            raise ValueError(f'The file {self.file_path} doesnt Exits')
