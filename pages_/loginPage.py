from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from common_.utilities_.customLogger import *


class LogInPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__usernameFieldLocator = (By.ID, "ap_email")
        self.__passwordFieldLocator = (By.ID, "ap_password")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__signInButtonLocator = (By.ID, "signInSubmit")
        self.__errorMessageYourPasswordIsIncorrectLocator = (By.CLASS_NAME, "a-list-item")
        self.__errorMessageWeCannotFindAnAccountWithThatEmailLocator = (By.CLASS_NAME, "a-list-item")
    def fill_username_field(self, userName):
        userNameFieldElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(userNameFieldElement, userName)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click_to_element(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFieldElement, password)

    def click_to_sign_in_button(self):
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        self._click_to_element(signInButtonElement)

    def validate_continue_button_text(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        if self._get_element_text(continueButtonElement) != "Continue":
            logger("ERROR", "Wrong 'continue' button text")
            exit(2)

    def validate_signin_button_text(self):
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        if self._get_element_text(signInButtonElement) != "Sign in":
            logger("ERROR", "Wrong 'Sign in' button text")
            exit(3)

    def validate_wrong_password_message(self):
        errorMessageYourPasswordIsIncorrectElement = self._get_element_text_by_locator(self.__errorMessageYourPasswordIsIncorrectLocator)
        logger("WARNING", "Your password is incorrect")
        return errorMessageYourPasswordIsIncorrectElement == "Your password is incorrect"

    def validate_wrong_username_message(self):
        errorMessageWeCannotFindAnAccountWithThatEmailElement = self._get_element_text_by_locator(self.__errorMessageWeCannotFindAnAccountWithThatEmailLocator)
        logger("WARNING", "We cannot find an account with that email address" )
        return errorMessageWeCannotFindAnAccountWithThatEmailElement == "We cannot find an account with that email address"
