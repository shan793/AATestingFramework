import datetime

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
import calendar
from datetime import date


class SearchResultsPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    search_results_page_header = (By.XPATH, "//h1[@id='aa-pageTitle' and contains(text(), 'Choose flights')]")
    search_results_page_header_XPath = "//h1[@id='aa-pageTitle' and contains(text(), 'Choose flights')]"

    departure_and_arrival_cities = (By.XPATH, "//span[@class='visible-phone']")
    departure_and_arrival_cities_XPath = "//span[@class='visible-phone']"

    date_of_depart_and_arrival = (By.XPATH, "//div[@id = 'flight-summary']/h3")
    date_of_depart_and_arrival_XPath = "//div[@id = 'flight-summary']/h3"

    first_origin_search_result_dynamic_XPath = "//div[@class='span4 span-phone6']/span[@class='flight-airport-code' and contains(text(), '{}')]"
    first_arrival_search_result_dynamic_XPath = "//div[@class='span4 span-phone5']/span[@class='flight-airport-code' and contains(text(), '{}')]"
    type_of_trip_in_search_results_validation_dynamic_XPath = "(//div[@class='triptype']['{}'])"
    select_fare_dynamic_XPath = "//button[@data-farename='{}']"


    @property
    def get_search_results_page_header(self):
        return self.driver.find_element(*SearchResultsPage.search_results_page_header)

    @property
    def get_departure_and_arrival_cities(self):
        return self.driver.find_element(*SearchResultsPage.departure_and_arrival_cities)

    @property
    def get_date_of_depart_and_arrival(self):
        return self.driver.find_element(*SearchResultsPage.date_of_depart_and_arrival)

    def validate_correct_departure_date(self, expected_month_as_int, expected_date_as_int, expected_year_as_int):
        expected_month_as_string = calendar.month_name[expected_month_as_int]
        split_up_date_string = []
        split_up_date_string = self.get_date_of_depart_and_arrival.text.replace(" ", "").split(",")
        day_of_dep = calendar.day_name[datetime.date(expected_year_as_int, expected_month_as_int, expected_date_as_int).weekday()]

        assert (expected_month_as_string in split_up_date_string[1]
                and str(expected_date_as_int) in split_up_date_string[1]
                and str(expected_year_as_int) in split_up_date_string[2]
                and day_of_dep == split_up_date_string[0])

    def check_origin_arrival_type(self, origin, arrival, trip_type):
        exception_handling = self.get_exception_handling()
        assert exception_handling.is_displayed_enhanced(self.first_origin_search_result_dynamic_XPath.format(origin.upper()), 5, self.driver)
        assert exception_handling.is_displayed_enhanced(self.first_arrival_search_result_dynamic_XPath.format(arrival.upper()), 5, self.driver)

        type_of_trip_in_search_results_validation = self.driver.find_element(By.XPATH, self.type_of_trip_in_search_results_validation_dynamic_XPath.format(trip_type.capitalize()))
        assert type_of_trip_in_search_results_validation.text == trip_type.capitalize()

    def select_class_and_fare(self, classType):
        if classType == "Main Cabin":
            classType = classType.replace(" ", "")
        else:
            classType = classType.capitalize()

        exception_handling = self.get_exception_handling()
        assert exception_handling.is_displayed_enhanced(self.select_fare_dynamic_XPath.format(classType), 5, self.driver)
        fare_to_select = self.driver.find_element(By.XPATH, self.select_fare_dynamic_XPath.format(classType))
        selected_fare = fare_to_select.get_attribute("data-fare-amount")
        print(selected_fare)
        fare_to_select.click()
        return selected_fare





