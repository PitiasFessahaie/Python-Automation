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
