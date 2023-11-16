from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common_.utilities_.customLogger import *


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            logger("INFO", f"Element with locator: {locator[1]} found")
            return element
        except:
            logger("ERROR", "Element Not found")
            exit(1)

    def _click_to_element(self, webElement):
        webElement.click()

    def _fill_field(self, webElement, text):
        webElement.clear()
        webElement.send_keys(text)

    def _get_title(self):
        logger("INFO", f"Title founded, title is {self.driver.title}")
        return self.driver.title

    def _get_element_text(self, element):
        return element.text

    def _get_element_text_by_locator(self, locator):
        element = self._find_element(locator)
        return element.text

