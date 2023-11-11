from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class ProductDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__addToCartButtonLocator = (By.ID, "add-to-cart-button")

    def click_to_add_to_cart_button(self):
        addToCartButton = self._find_element(self.__addToCartButtonLocator)
        self._click_to_element(addToCartButton)
