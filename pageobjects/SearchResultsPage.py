from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class SearchResultsPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    search_results_page_header = (By.XPATH, "//h1[@id='aa-pageTitle' and contains(text(), 'Choose flights')]")
    search_results_page_header_XPath = "//h1[@id='aa-pageTitle' and contains(text(), 'Choose flights')]"

    departure_and_arrival_cities = (By.XPATH, "//span[@class='visible-phone']")
    departure_and_arrival_cities_XPath = "//span[@class='visible-phone']"

    first_origin_search_result_dynamic_XPath = "//div[@class='span4 span-phone6']/span[@class='flight-airport-code' and contains(text(), '{}')]"
    first_arrival_search_result_dynamic_XPath = "//div[@class='span4 span-phone5']/span[@class='flight-airport-code' and contains(text(), '{}')]"
    type_of_trip_in_search_results_validation_dynamic_XPath = "(//div[@class='triptype']['{}'])"


    @property
    def get_search_results_page_header(self):
        return self.driver.find_element(*SearchResultsPage.search_results_page_header)

    @property
    def get_departure_and_arrival_cities(self):
        return self.driver.find_element(*SearchResultsPage.departure_and_arrival_cities)

    def check_origin_arrival_type(self, origin, arrival, trip_type):
        exception_handling = self.get_exception_handling()
        exception_handling.is_displayed_enhanced(self.first_origin_search_result_dynamic_XPath.format(origin.upper()), 5, self.driver)
        exception_handling.is_displayed_enhanced(self.first_arrival_search_result_dynamic_XPath.format(arrival.upper()), 5, self.driver)

        type_of_trip_in_search_results_validation = self.driver.find_element(By.XPATH, self.type_of_trip_in_search_results_validation_dynamic_XPath.format(trip_type.capitalize()))
        assert type_of_trip_in_search_results_validation.text == trip_type.capitalize()


