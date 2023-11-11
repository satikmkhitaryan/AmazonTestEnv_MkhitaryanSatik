from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            print(f"Element with locator: {locator[1]} found")
            return element
        except:
            print("Error: Element Not found")
            exit(1)

    def _click_to_element(self, webElement):
        webElement.click()

    def _fill_field(self, webElement, text):
        webElement.clear()
        webElement.send_keys(text)

    def _get_title(self):
        return self.driver.title

    def _get_element_text(self, element):
        return element.text

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
# from common_.utilities_.customLogger import *
#
#
# class BasePage:
#     def __init__(self, driver: webdriver.Chrome):
#         self.driver = driver
#
#     def _find_element(self, locator, timeout=10, condition=EC.visibility_of_element_located):
#         try:
#             element = WebDriverWait(self.driver, timeout).until(condition(locator))
#             return element
#         except NoSuchElementException as e:
#             logger("ERROR", "Element not visible but should be")
#             exit(1)
#         except TimeoutException as e:
#             logger("ERROR", f"Timeout waiting for element: {str(e)}")
#             exit(2)
#
#     def _get_title(self):
#         logger("INFO", f"Title founded, title is {self.driver.title}")
#         return self.driver.title
#
#     def _fill_field(self, element, text):
#         element.clear()
#         element.send_keys(text)
#
#     def _fill_field_and_apply(self, element, text, key):
#         self._fill_field(element, text)
#         element.send_keys(key)
#
#     def _click_to_element(self, element):
#         try:
#             WebDriverWait(self.driver, 10).until(lambda driver: element.is_enabled() and element.is_displayed())
#         except TimeoutException as e:
#             logger("ERROR", f"Timeout waiting for the element to be clickable: {str(e)}")
#             exit(2)
#         except ElementClickInterceptedException as e:
#             logger("ERROR", f"Element is not clickable due to interception: {str(e)}")
#             exit(4)
#         except Exception as e:
#             logger("ERROR", f"An unexpected error occurred: {str(e)}")
#             exit(1)
#         element.click()
#
#     def _get_element_text(self, element):
#         return element.text
#
#     def _double_click_to_element(self, element):
#         try:
#             WebDriverWait(self.driver, 10).until(
#                 lambda driver: element.is_enabled() and element.is_displayed()
#             )
#         except TimeoutException as e:
#             logger("ERROR", f"Timeout waiting for the element to be clickable: {str(e)}")
#             exit(2)
#         except ElementClickInterceptedException as e:
#             logger("ERROR", f"Element is not clickable due to interception: {str(e)}")
#             exit(4)
#         except Exception as e:
#             logger("ERROR", f"An unexpected error occurred: {str(e)}")
#             exit(5)
#
#         action = ActionChains(self.driver)
#         action.double_click(element)
#         action.perform()
#
#     def _element_should_be_visible(self, locator, timeout=10):
#         try:
#             element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
#             return element.is_displayed()
#         except TimeoutException as e:
#             logger("ERROR", f"Timeout waiting for the element to be visible : {str(e)}")
#             exit(2)
#         except Exception as e:
#             logger("ERROR", f"An unexpected error occurred: {str(e)}")
#             exit(5)
#
#     def _element_should_be_clickable(self, locator, timeout=10):
#         try:
#             WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
#         except:
#             logger("ERROR", f"Element located by {locator} is not clickable, but should be:")
#             exit(4)
