from pageobjects.Homepage import HomePage
from pageobjects.SearchResultsPage import SearchResultsPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    # This first test login is still pointing to the delta website and it's locators
    # Will have to update this to use the AA flow, Had to stop delta framework,
    # Since delta website does not allow for automation testing
    #     def test_login(self):
    #         homepage = HomePage(self.driver)
    #         logger = self.getLogger()
    #         actions = self.get_actions()
    #
    #         self.validate_page_has_appeared(homepage.get_login_button_home_page)
    #         self.click_to_close(homepage.get_alert_advisory_close_button)
    #
    #         loginpage = homepage.click_login_button()
    #         self.validate_page_has_appeared(loginpage.get_login_page_header)
    #
    #         loginpage.login_to_delta("shihabSylhetTestOne", "Sylhettest", "$shihabSylhetTest1")
    #         homepage.validate_username_of_homepage_logged_in("Shihabtest")
    #         print("Test passed")

    def test_search_for_flight(self):
        homepage = HomePage(self.driver)
        search_results_page = SearchResultsPage(self.driver)

        homepage.enter_cities_to_travel_to("DFW", "CMB")
        homepage.select_type_of_trip("One Way")
        homepage.pax_count_picker(5)
        homepage.date_picker(1, 5, 2023)
        homepage.hover_over_and_click_search_for_flights_button()
        self.validate_page_has_appeared(search_results_page.search_results_page_header_XPath, 60)
        search_results_page.validate_correct_departure_date(1, 5, 2023)
        search_results_page.check_origin_arrival_type("DFW", "CMB", "One Way")
        search_results_page.select_class_and_fare("First")

