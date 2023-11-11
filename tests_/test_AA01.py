import unittest
from time import sleep
from selenium import webdriver
from testData_ import testData
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from pages_.loginPage import LogInPage



class AA_01(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(testData.urlSignIn)

    def test_positive_login(self):
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field(testData.loginDataValid["username"])
        logInPageObj.validate_continue_button_text()
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_field(testData.loginDataValid["password"])
        # Here we put sleep so as not to be perceived as a robot
        sleep(10)
        logInPageObj.click_to_sign_in_button()
        sleep(5)

    def test_negative_login(self):
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field(testData.loginDataWithInvalidPassword["username"])
        logInPageObj.validate_continue_button_text()
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_field(testData.loginDataWithInvalidPassword["password"])
        # Here we put sleep so as not to be perceived as a robot
        sleep(10)
        logInPageObj.click_to_sign_in_button()


    def tearDown(self):
        self.driver.close()
