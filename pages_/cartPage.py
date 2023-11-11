from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "(//input[@value='Delete'])[2]")
        self.__saveForLaterForFirstProductButtonLocator = (By.XPATH, "(//input[@class='a-color-link'])[1]")

    def delete_first_product_from_cart(self):
        firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
        self._click(firstProductDeleteButtonElement)

    def click_to_save_for_later_for_first_product_button(self):
        saveForLaterForFirstProductButton = self._find_element(self.__saveForLaterForFirstProductButtonLocator)
        self._click(saveForLaterForFirstProductButton)
