from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import *


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "(//input[@value='Delete'])[1]")
        self.__saveForLaterForFirstProductButtonLocator = (By.XPATH, "(//input[@class='a-color-link'])[1]")
        self.__yourAmazonCartIsEmptyMessageLocator = (By.XPATH, "//h1[@class = 'a-spacing-mini a-spacing-top-base']")
        self.__cartButtonLocator = (By.ID, "nav-cart-count")
        self.__addedToCartMessageLocator = (By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS")
        self.__firstProductCountLocator = (By.XPATH, "(//span[@class='a-dropdown-prompt'])[1]")

    def get_first_product_count(self):
        firstProductCountElement = self._find_element(self.__firstProductCountLocator)
        return int(self._get_element_text(firstProductCountElement))

    def delete_first_product_from_cart(self):
        firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
        self._click_to_element(firstProductDeleteButtonElement)

    def delete_all_products_from_cart(self):
        from pages_.navigationBar_.navigationBar import NavigationBar
        navigationBarPage = NavigationBar(self.driver)
        while navigationBarPage.get_product_count_in_cart() != 0:
            firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
            self._click_to_element(firstProductDeleteButtonElement)
        logger("INFO", "Your Amazon cart is already empty")

    def click_to_save_for_later_for_first_product_button(self):
        saveForLaterForFirstProductButton = self._find_element(self.__saveForLaterForFirstProductButtonLocator)
        self._click_to_element(saveForLaterForFirstProductButton)

    def validate_Amazon_cart_emptiness_with_message(self):
        yourAmazonCartIsEmptyMessageElement = self._find_element(self.__yourAmazonCartIsEmptyMessageLocator)
        yourAmazonCartIsEmptyMessageText = self._get_element_text(yourAmazonCartIsEmptyMessageElement)
        assert yourAmazonCartIsEmptyMessageText == "Your Amazon Cart is empty."
        logger("ERROR", "Cart is not empty but should be empty")

    def is_added_to_cart_message_appear(self):
        addedToCartMessageElement = self._find_element(self.__addedToCartMessageLocator)
        addedToCartMessageText = self._get_element_text(addedToCartMessageElement)
        return addedToCartMessageText == "Added to Cart"
