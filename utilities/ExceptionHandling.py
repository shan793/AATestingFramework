import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class ExceptionHandling:

    def __init__(self, driver):
        self.driver = driver

    def is_displayed_enhanced(self, element_to_check_xpath, time_to_wait_for_element_in_seconds, driver):
        self.driver.implicitly_wait(time_to_wait_for_element_in_seconds)
        is_element_displayed = True

        try:
            is_element_displayed = self.driver.find_element(By.XPATH, element_to_check_xpath).is_displayed()
        except NoSuchElementException as e:
            print(f"Element: {element_to_check_xpath} was not displayed, returning false")
            is_element_displayed = False

        self.driver.implicitly_wait(30)
        return is_element_displayed
