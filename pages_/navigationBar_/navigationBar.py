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
        self.__changeLanguageButtonLocator = (By.ID, "icp-nav-flyout")
        self.__espanolIconLocator = (By.XPATH, "(//*[@dir='ltr'])[4]")
        self.__accountsAndListsButtonLocator = (By.ID, "nav-link-accountList")
        self.__signOutButtonLocator = (By.ID, "nav-item-signout")

    def click_to_change_language_icon(self):
        changeLanguageButtonElement = self._find_element(self.__changeLanguageButtonLocator)
        self._click_to_element(changeLanguageButtonElement)


    def change_language_to_espanol(self):
        changeLanguageButtonElement = self._find_element(self.__changeLanguageButtonLocator)
        self._mouse_move(changeLanguageButtonElement)
        espanolIconElement = self._find_element(self.__espanolIconLocator)
        self._click_to_element(espanolIconElement)

    def click_to_main_page_button(self):
        mainPageButtonElement = self._find_element(self.__mainPageButtonLocator)
        self._click_to_element(mainPageButtonElement)

    def move_to_account_and_lists_button(self):
        accountsAndListsButtonElement = self._find_element(self.__accountsAndListsButtonLocator)
        self._mouse_move(accountsAndListsButtonElement)

    def click_to_sign_out_button(self):
        signOutButtonElement = self._find_element(self.__signOutButtonLocator)
        self._click_to_element(signOutButtonElement)

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
        return int(cartButtonElementText)

    def click_to_change_language_icon(self):
        changeLanguageButtonElement = self._find_element(self.__changeLanguageButtonLocator)
        self._click_to_element(changeLanguageButtonElement)

    def click_to_espanol_icon(self):
        changeLanguageButtonElement = self._find_element(self.__changeLanguageButtonLocator)
        self._mouse_move(changeLanguageButtonElement)
        espanolIconElement = self._find_element(self.__espanolIconLocator)
        self._click_to_element(espanolIconElement)

    def validate_language_icon_text(self, language):
        changeLanguageButtonElement = self._find_element(self.__changeLanguageButtonLocator)
        changeLanguageButtonText = self._get_element_text(changeLanguageButtonElement)
        if changeLanguageButtonText == language:
            logger("INFO", f"It's true. The language is {language}")
            return True
        else:
            return False



