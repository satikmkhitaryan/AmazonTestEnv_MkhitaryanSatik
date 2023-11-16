from selenium.webdriver.support.events import AbstractEventListener
from common_.utilities_.customLogger import logger


class MyListener(AbstractEventListener):
    def after_find(self, by, value, driver):
        logger("INFO", f"Founded element with locator: By: {by}, Value: {value}")

    def after_click(self, element, driver):
        logger("INFO", f"Clicked to element: {element}" )

    def after_change_value_of(self, element, driver):
        logger("INFO", f"Changed value of element: {element}")

    def after_execute_script(self, script, driver):
        logger("INFO",  "after_execute_script")


    def after_close(self, driver):
        logger("INFO", f"Closing browser")

    def after_quit(self, driver):
        logger("INFO", f"Quiting browser tab")

