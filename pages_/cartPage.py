from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import *


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "(//input[@value='Delete'])[1]")
        self.__saveForLaterForFirstProductButtonLocator = (By.XPATH, "(//input[@class='a-color-link'])[1]")
        self.__yourAmazonCartIsEmptyMessageLocator = (By.CLASS_NAME, "a-spacing-mini a-spacing-top-base")

    def delete_first_product_from_cart(self):
        firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
        self._click_to_element(firstProductDeleteButtonElement)

    def delete_all_products_from_cart(self, productsCountInCart):
        for i in range(productsCountInCart):
            firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
            self._click_to_element(firstProductDeleteButtonElement)

    def click_to_save_for_later_for_first_product_button(self):
        saveForLaterForFirstProductButton = self._find_element(self.__saveForLaterForFirstProductButtonLocator)
        self._click_to_element(saveForLaterForFirstProductButton)

    def validate_your_Amazon_cart_is_empty_message(self):
        yourAmazonCartIsEmptyMessageElement = self._get_element_text_by_locator(self.__yourAmazonCartIsEmptyMessageLocator)
        logger("WARNING", "Your Amazon Cart is empty")
        return yourAmazonCartIsEmptyMessageElement == "Your Amazon Cart is empty."