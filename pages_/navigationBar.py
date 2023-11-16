from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import *


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__mainPageButtonLocator = (By.ID, "nav-logo-sprites")
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")
        self.__cartButtonLocator = (By.ID, "nav-cart-count")

    def click_to_main_page_button(self):
        mainPageButton = self._find_element(self.__mainPageButtonLocator)
        self._click_to_element(mainPageButton)

    def fill_search_field(self, productName):
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._fill_field(searchFieldElement, productName)

    def click_to_search_button(self):
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click_to_element(searchButtonElement)

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click_to_element(cartButtonElement)

    def get_product_count_in_cart(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        cartButtonElementText = self._get_element_text(cartButtonElement)
        return cartButtonElementText

