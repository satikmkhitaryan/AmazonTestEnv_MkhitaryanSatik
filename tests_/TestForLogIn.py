import unittest
from time import sleep
from selenium import webdriver
from testData_ import testData
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from pages_.loginPage import LogInPage
from common_.utilities_.customLogger import *


# Description: Create test for Sign in functionality in Amazon.com
class login_test(unittest.TestCase):
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
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_field(testData.loginDataValid["password"])
        sleep(6)  # Here we put sleep so as not to be perceived as a robot
        # self.assertTrue(logInPageObj.get_signin_button_text(), "ERROR: Wrong 'Sign in' button text")
        logInPageObj.click_to_sign_in_button()
        sleep(10)
        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title, "You could not signed in successfully ")

    def test_negative_login_with_invalid_password(self):
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field(testData.loginDataWithInvalidPassword["username"])
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_field(testData.loginDataWithInvalidPassword["password"])
        sleep(10)  # Here we put sleep so as not to be perceived as a robot
        logInPageObj.click_to_sign_in_button()
        sleep(5)
        self.assertTrue(logInPageObj.is_wrong_password_error_message_appear(), "Error: Should see a message about incorrect password but it did not show")

    def test_negative_login_with_invalid_logipn(self):
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field(testData.loginDataWithInvalidUsername["username"])
        logInPageObj.click_to_continue_button()
        self.assertTrue(logInPageObj.is_wrong_username_error_message_appear(), "Error: Should see a message about incorrect email address/mobile but it did not show")

    def tearDown(self):
        self.driver.close()
