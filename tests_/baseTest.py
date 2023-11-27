import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from testData_.testData import urlSignInPage, urlMainPage, userWithValidData
from pages_.logInPage_.loginPage import LogInPage
from time import sleep


class BaseTestWithoutLogIn(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(urlMainPage)

    def tearDown(self):
        self.driver.close()


class BaseTestWithLogIn(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(urlSignInPage)

        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field(userWithValidData.userName)
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_field(userWithValidData.password)
        sleep(10)  # Here we put sleep so as not to be perceived as a robot
        logInPageObj.click_to_sign_in_button()

    def tearDown(self):
        self.driver.close()
