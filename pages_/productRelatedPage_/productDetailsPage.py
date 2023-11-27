from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class ProductDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__addToCartButtonLocator = (By.ID, "add-to-cart-button")
        self.__productNameLocator = (By.ID, "title")
        self.__productPriceLocator = (By.ID, "corePriceDisplay_desktop_feature_div")

    def click_to_add_to_cart_button(self):
        addToCartButton = self._find_element(self.__addToCartButtonLocator)
        self._click_to_element(addToCartButton)

    def get_product_name(self):
        productNameElement = self._find_element(self.__productNameLocator)
        return self._get_element_text(productNameElement)

    def get_product_price(self):
        productPriceElement = self._find_element(self.__productPriceLocator)
        return self._get_element_text(productPriceElement)

