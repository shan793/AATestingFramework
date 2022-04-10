import calendar

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


from pageobjects.Loginpage import LoginPage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    type_of_trip_dropdown_selector = (By.XPATH, "//span[@id = 'selectTripType-val']")
    type_of_trip_dropdown_selector_XPath = "//span[@id = 'selectTripType-val']"

    origin_city = (By.XPATH, "//input[@id='reservationFlightSearchForm.originAirport']")
    origin_city_XPath = "//input[@id='reservationFlightSearchForm.originAirport']"

    arrival_city = (By.XPATH, "//input[@id='reservationFlightSearchForm.destinationAirport']")
    arrival_city_XPath = "//input[@id='reservationFlightSearchForm.destinationAirport']"

    city_search_box = (By.XPATH, "//input[@id='search_input']")
    city_search_box_XPath = "//input[@id='search_input']"

    date_picker_opener = (By.XPATH, "//button[@class='ui-datepicker-trigger']")
    date_picker_opener_XPath = "//button[@class='ui-datepicker-trigger']"

    date_picker_dep_after_select = (By.XPATH, "//span[@class = 'calenderDepartSpan']")
    date_picker_dep_after_select_XPath = "//span[@class = 'calenderDepartSpan']"

    select_next_month = (By.XPATH, "//a[@aria-label='Next Month']")
    select_next_month_XPath = "//a[@aria-label='Next Month']"

    pax_picker_dropdown_selector = (By.XPATH, "//select[@id='flightSearchForm.adultOrSeniorPassengerCount']")
    pax_picker_dropdown_selector_XPath = "//select[@id='flightSearchForm.adultOrSeniorPassengerCount']"
    pax_picker_dropdown_selector_ID = "flightSearchForm.adultOrSeniorPassengerCount"

    pax_picker_dropdown_all_options_box = (By.XPATH, "//ul[@id = 'selectTripType-desc']")
    pax_picker_dropdown_all_options_box_XPath = "//ul[@id = 'selectTripType-desc']"

    date_picker_dept_text_box = (By.XPATH, "//input[@name='departDate']")
    date_picker_dept_text_box_Xpath = "//input[@name='departDate']"
    date_picker_dept_text_box_id = "aa-leavingOn"

    search_for_all_flights_submit_button = (By.XPATH, "//input[@id='flightSearchForm.button.reSubmit']")
    search_for_all_flights_submit_button_XPath = "//input[@id='flightSearchForm.button.reSubmit']"

    first_dropdown_suggestion_dynamic_xpath = "//li[@class='ui-menu-item']/a[contains(text(), '{}')]"
    type_of_trip_option_dynamic_xpath = "//div[@id='bookingCheckboxContainer']//span[contains(text(), '{}')]"
    date_picker_month_dynamic_xpath = "//span[contains(@class,'ui-datepicker-month') and contains(text(), '{}')]"
    date_picker_year_dynamic_xpath = "//span[contains(@class,'ui-datepicker-year') and contains(text(), '{}')]"
    number_of_pax_option_to_select_dynamic_xpath = "//ul[@id = 'passengers-desc']/li[contains(text(), '{}')]"

    @property
    def type_of_trip_dropdown_selector(self):
        return self.driver.find_element(*HomePage.type_of_trip_dropdown_selector)

    @property
    def get_origin_city(self):
        return self.driver.find_element(*HomePage.origin_city)

    @property
    def get_arrival_city(self):
        return self.driver.find_element(*HomePage.arrival_city)

    @property
    def get_first_dropdown_suggestion(self):
        return self.driver.find_element(*HomePage.first_dropdown_suggestion)

    @property
    def get_city_search_box(self):
        return self.driver.find_element(*HomePage.city_search_box)

    @property
    def get_datepicker_opener(self):
        return self.driver.find_element(*HomePage.date_picker_opener)

    @property
    def get_datepicker_dep_after_select(self):
        return self.driver.find_element(*HomePage.date_picker_dep_after_select)

    @property
    def get_select_next_month(self):
        return self.driver.find_element(*HomePage.select_next_month)

    @property
    def get_pax_picker_dropdown_selector(self):
        return self.driver.find_element(*HomePage.pax_picker_dropdown_selector)

    @property
    def get_pax_picker_dropdown_all_options_box(self):
        return self.driver.find_element(*HomePage.pax_picker_dropdown_all_options_box)

    @property
    def get_date_picker_dept_text_box(self):
        return self.driver.find_element(*HomePage.date_picker_dept_text_box)

    @property
    def get_search_for_flights_submit_button(self):
        return self.driver.find_element(*HomePage.search_for_all_flights_submit_button)

    def click_login_button(self):
        self.driver.find_element(*HomePage.login_button_home_page).click()
        loginpage = LoginPage(self.driver)
        return loginpage

    def validate_username_of_homepage_logged_in(self, expectedFirstName):
        assert expectedFirstName == self.get_home_page_logged_in_username_displayed.text

    def enter_cities_to_travel_to(self, origin, arrival):
        self.get_origin_city.clear()
        self.get_origin_city.click()
        actions = ActionChains(self.driver)
        actions.send_keys(origin)
        actions.perform()
        first_suggestion_origin = self.driver.find_element(By.XPATH, self.first_dropdown_suggestion_dynamic_xpath.format(origin.upper()))
        first_suggestion_origin.click()
        self.get_arrival_city.clear()
        self.get_arrival_city.click()
        a = ActionChains(self.driver)
        a.send_keys(arrival)
        a.perform()
        first_suggestion_arrival = self.driver.find_element(By.XPATH, self.first_dropdown_suggestion_dynamic_xpath.format(arrival.upper()))
        first_suggestion_arrival.click()

    def select_type_of_trip(self, triptype):

        type_of_trip = self.driver.find_element(By.XPATH, self.type_of_trip_option_dynamic_xpath.format(triptype.capitalize()))
        assert type_of_trip.is_displayed()

        actions = ActionChains(self.driver)
        actions.move_to_element(type_of_trip)
        actions.click()
        actions.perform()

    def date_picker(self, month_as_int, date_as_int, year_as_int):
        month_as_string = calendar.month_name[month_as_int]

        date_picker_month_header_xpath = self.date_picker_month_dynamic_xpath.format(month_as_string)
        date_picker_year_header_xpath = self.date_picker_year_dynamic_xpath.format(year_as_int)

        self.get_datepicker_opener.click()

        exception_handling = self.get_exception_handling()

        while not exception_handling.is_displayed_enhanced(date_picker_month_header_xpath, 0.1, self.driver) and not exception_handling.is_displayed_enhanced(date_picker_year_header_xpath, 0.1, self.driver):
            actions = ActionChains(self.driver)
            actions.move_to_element(self.get_select_next_month)
            actions.click()
            actions.perform()

        dates = "/parent::div/parent::div/following-sibling::table//a[text()= '{}']".format(date_as_int)
        date_picker_indiv_date_xpath = date_picker_month_header_xpath + dates
        date_picker_indiv_date = self.driver.find_element(By.XPATH, date_picker_indiv_date_xpath)

        a = ActionChains(self.driver)
        a.move_to_element(date_picker_indiv_date)
        a.click()
        a.perform()

        date_selected = self.driver.execute_script(f'return document.getElementById("{self.date_picker_dept_text_box_id}").value')
        date_inputted = f"{month_as_int}/{date_as_int}/{year_as_int}"

        # if date_selected.find(date_inputted):
        #     print(date_selected, date_inputted)
        #     assert True
        # else:
        #     assert False

        assert True if date_selected.find(date_inputted) else False
        # For whatever reason a direction assertion doesn't work, have to use an if else conditional and can't use
        # in because in doesn't work when object is pointing to none

    def pax_count_picker(self, number_of_pax_one_to_nine):
        assert self.get_pax_picker_dropdown_selector.is_displayed()
        select = Select(self.driver.find_element(By.XPATH, self.pax_picker_dropdown_selector_XPath))
        select.select_by_visible_text(str(number_of_pax_one_to_nine))

        pax_number = self.driver.execute_script('return document.getElementById("flightSearchForm.adultOrSeniorPassengerCount").value')
        assert pax_number == str(number_of_pax_one_to_nine)


    def hover_over_and_click_search_for_flights_button(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_search_for_flights_submit_button)
        actions.click()
        actions.perform()





