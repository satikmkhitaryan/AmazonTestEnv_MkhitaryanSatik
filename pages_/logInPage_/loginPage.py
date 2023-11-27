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
        self.__signInButtonLocator = (By.ID, "auth-signin-button")
        self.__errorMessageYourPasswordIsIncorrectLocator = (By.CLASS_NAME, "a-list-item")
        self.__errorMessageWeCannotFindAnAccountWithThatEmailLocator = (By.CLASS_NAME, "a-list-item")
        self.__signInTextLocator = (By.CLASS_NAME, "a-spacing-small")

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

    def get_signin_button_text(self):
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        signInButtonText = self._get_element_text(signInButtonElement)
        return signInButtonText

    def is_wrong_password_error_message_appear(self):
        errorMessageYourPasswordIsIncorrectElement = self._find_element(self.__errorMessageYourPasswordIsIncorrectLocator)
        errorMessageYourPasswordIsIncorrectText = self._get_element_text(errorMessageYourPasswordIsIncorrectElement)
        if errorMessageYourPasswordIsIncorrectText == "Your password is incorrect":
            logger("WARNING", "Your password is incorrect")
            return True
        else:
            return False

    def is_wrong_username_error_message_appear(self):
        errorMessageWeCannotFindAnAccountWithThatEmailElement = self._find_element(self.__errorMessageWeCannotFindAnAccountWithThatEmailLocator)
        errorMessageWeCannotFindAnAccountWithThatEmailText = self._get_element_text(errorMessageWeCannotFindAnAccountWithThatEmailElement)
        if errorMessageWeCannotFindAnAccountWithThatEmailText == "We cannot find an account with that email address":
            logger("WARNING", "There was a problem. Your email address/mobile number is incorrect.")
            return True
        else:
            return False

    def is_sign_in_text_appear(self):
        signInTextElement = self._find_element(self.__signInTextLocator)
        logger("INFO", "You are Sign out from Amazon.com successfully ")
        return self._get_element_text(signInTextElement)
