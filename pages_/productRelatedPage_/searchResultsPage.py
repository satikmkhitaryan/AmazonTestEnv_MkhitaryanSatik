from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductLocator = (By.XPATH, "(//img[@class='s-image'])[1]")
        self.__firstProductNameLocator = (By.XPATH, "(//span[@class='a-size-base-plus a-color-base a-text-normal'])[1]")
        self.__firstProductPriceLocator = (By.XPATH, "(//span[@class='a-price'])[1]")

    def click_to_first_product(self):
        firstProductElement = self._find_element(self.__firstProductLocator)
        self._click_to_element(firstProductElement)

    def get_first_product_name(self):
        firstProductNameElement = self._find_element(self.__firstProductNameLocator)
        return self._get_element_text(firstProductNameElement)

    def get_first_product_price(self):
        firstProductPriceElement = self._find_element(self.__firstProductPriceLocator)
        return self._get_element_text(firstProductPriceElement)

