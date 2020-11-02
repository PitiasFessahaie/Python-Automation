from selenium.webdriver.common.by import By


class Locator:
    # Login success Page

    username = (By.CSS_SELECTOR, '#username')
    password = (By.CSS_SELECTOR, '#password')
    login = (By.CSS_SELECTOR, '.radius')
    login_url = 'http://localhost:7080/login'

    # Login_Failure Page
    username1 = (By.CSS_SELECTOR, '#username')
    password1 = (By.CSS_SELECTOR, '#password')
    login1 = (By.CSS_SELECTOR, '.radius')
    login_url = 'http://localhost:7080/login'

    # Drag and Drop Page
    dd_url = 'http://localhost:7080/drag_and_drop'
    Abox = '#column-a'
    Bbox = '#column-b'

    # Check_Box Page
    checkbox_url = 'http://localhost:7080/checkboxes'
    checkbox1 = '//body//input[1]'
    checkbox2 = '//body//input[2]'

    # Context_Menu
    context_url = 'http://localhost:7080/context_menu'
    right_click = '#hot-spot'

    # drop Down
    dropDown_url = 'http://localhost:7080/dropdown'
    dropDown_btn = '#dropdown'

    # Dynamic_Control
    url_dynamicControl = 'http://localhost:7080/dynamic_controls'
    add_btn = (By.XPATH, "//*[@onclick='swapCheckbox()']")
    add_msg = (By.XPATH, "//*[@type='checkbox']")
    remove_btn = "//*[@id='checkbox-example']/button"
    enable_btn = (By.XPATH, "//*[@onclick='swapCheckbox()']")
    enable_txt = "//p[@id='message']"
    disable_btn = (By.XPATH, "//*[@onclick='swapInput()']")
    disable_msg = "//p[@id='message']"

    # IFrame
    url_iframe = 'http://localhost:7080/iframe'
    itext_field = '#tinymce'
    # File Download
    file_path = '/Users/pitiasfessahaie/Downloads/some-file.txt'
    url_Filedownload = 'http://localhost:7080/download'
    file = '//*[@id="content"]/div/a[1]'