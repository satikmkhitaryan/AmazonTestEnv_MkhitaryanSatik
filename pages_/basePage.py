from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
        logger("INFO", f"The {webElement} element is clicked")

    def _fill_field(self, webElement, text):
        webElement.clear()
        webElement.send_keys(text)
        logger("INFO", f"The text is successfully added to {webElement} element")

    def _get_title(self):
        logger("INFO", f"Title founded, title is {self.driver.title}")
        return self.driver.title

    def _get_element_text(self, element):
        logger("INFO", f"Text is founded {element.text}")
        return element.text

    def _get_element_text_by_locator(self, locator):
        element = self._find_element(locator)
        logger("INFO", f"TText is founded {element.text} for {element} element")
        return element.text

    def _mouse_move(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        logger("INFO", f"Mouse moved to {element} element")

