from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__firstProductLocator = (By.XPATH, "(//img[@class='s-image'])[1]")

    def click_to_first_product(self):
        firstProductElement = self._find_element(self.__firstProductLocator)
        self._click_to_element(firstProductElement)