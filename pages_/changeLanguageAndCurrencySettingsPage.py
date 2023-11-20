from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import *


class ChangeLanguagePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__englishButtonLocator = (By.XPATH, "(//*[@class='a-label a-radio-label'])[1]")
        self.__currencyDropDownButtonLocator = (By.ID, "icp-currency-dropdown-selected-item-prompt")
        self.__armenianDramIconLocator = (By.ID, "AMD")
        self.__saveChangesButtonLocator = (By.ID, "icp-save-button")

    def click_to_english_language_button(self):
        englishButtonElement = self._find_element(self.__englishButtonLocator)
        self._click_to_element(englishButtonElement)

    def click_to_select_currency_drop_down_button(self):
        currencyDropDownButtonElement = self._find_element(self.__currencyDropDownButtonLocator)
        self._click_to_element(currencyDropDownButtonElement)

    def click_to_Armenian_Dram_Icon(self):
        armenianDramIconElement = self._find_element(self.__armenianDramIconLocator)
        self._click_to_element(armenianDramIconElement)

    def validate_currency_icon_text(self):
        currencyDropDownButtonElement = self._find_element(self.__currencyDropDownButtonLocator)
        self._get_element_text(currencyDropDownButtonElement)

    def click_to_save_changes_button(self):
        saveChangesButtonElement = self._find_element(self.__saveChangesButtonLocator)
        self._click_to_element(saveChangesButtonElement)


