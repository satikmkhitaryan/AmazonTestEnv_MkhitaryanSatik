from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__goToHomepageButtonLocator = (By.ID, "nav-logo-sprites")
        self.__productSearchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")
        self.__cartButtonLocator = (By.ID, "nav-cart-count")

    def click_to_go_to_homepage_button(self):
        goToHomepageButton = self._find_element(self.__goToHomepageButtonLocator)
        self._click(goToHomepageButton)

    def fill_search_field(self, product):
        productSearchFieldElement = self._find_element(self.__productSearchFieldLocator)
        self._fill_field(productSearchFieldElement, product)

    def click_to_search_button(self):
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click(searchButtonElement)

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click(cartButtonElement)

    def validate_count_of_products_in_cart(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        return self._get_element_text(cartButtonElement)
