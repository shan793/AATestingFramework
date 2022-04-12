from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    login_page_header = (By.XPATH, "//h1[contains(text(), 'To Delta')]")
    login_page_header_XPath = "//h1[contains(text(), 'To Delta')]"

    username_box = (By.XPATH, "//input[@id = 'userId']")
    username_box_XPath =  "//input[@id = 'userId']"

    lastname_box = (By.XPATH, "//input[@id = 'lastName']")
    lastname_box_XPath = "//input[@id = 'lastName']"

    password_box = (By.XPATH, "//input[@id = 'password']")
    password_box_XPath = "//input[@id = 'password']"

    password_reveal_button = (By.XPATH, "//button[@class = 'passwordIcon']")
    password_reveal_button_XPath = "//button[@class = 'passwordIcon']"

    keep_me_loggedin_checkbox = (By.XPATH, "//input[@id = 'persistentLogin_CheckBox']")
    keep_me_loggedin_checkbox_XPath = "//input[@id = 'persistentLogin_CheckBox']"

    login_button = (By.XPATH, "//div[@class = 'loginButtonDiv']/button[@type = 'submit']")
    login_button_XPath = "//div[@class = 'loginButtonDiv']/button[@type = 'submit']"

    @property
    def get_login_page_header(self):
        return self.driver.find_element(*LoginPage.login_page_header)

    @property
    def get_username_box(self):
        return self.driver.find_element(*LoginPage.username_box)

    @property
    def get_lastname_box(self):
        return self.driver.find_element(*LoginPage.lastname_box)

    @property
    def get_password_box(self):
        return self.driver.find_element(*LoginPage.password_box)

    @property
    def get_password_reveal_button(self):
        return self.driver.find_element(*LoginPage.password_reveal_button)

    @property
    def get_keep_me_loggedin_checkbox(self):
        return self.driver.find_element(*LoginPage.keep_me_loggedin_checkbox)

    @property
    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def login_to_delta(self, username, lastname, password):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_username_box)
        actions.click()
        actions.send_keys(username)
        actions.perform()

        assert self.get_password_box.is_displayed()

        a = ActionChains(self.driver)

        a.move_to_element(self.get_lastname_box)
        a.click()
        a.send_keys(lastname)
        a.move_to_element(self.get_password_reveal_button)
        a.click()
        a.move_to_element(self.get_password_box)
        a.click()
        a.send_keys(password)
        a.move_to_element(self.get_keep_me_loggedin_checkbox)
        a.click()
        a.move_to_element(self.get_login_button)
        a.click()
        a.perform()

