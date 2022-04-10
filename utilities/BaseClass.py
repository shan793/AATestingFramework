import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from utilities.ExceptionHandling import ExceptionHandling


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.setLevel(logging.DEBUG)
        return logger

    def get_exception_handling(self):
        exception_handling = ExceptionHandling(self.driver)
        return exception_handling

    def get_actions(self):
        actions = ActionChains(self.driver)
        return actions

    def verify_link_presence(self, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def validate_page_has_appeared(self, element):
        assert element.is_displayed()

    def click_to_close(self, element):
        assert element.is_displayed()
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.perform()

    def select_option_by_visible_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
