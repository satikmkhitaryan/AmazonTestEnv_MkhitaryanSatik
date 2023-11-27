from time import sleep
from pages_.logInPage_.loginPage import LogInPage
from testData_.testData import userWithValidData, urlSignInPage, userWithInvalidPassword, userWithInvalidUsername
from tests_.baseTest import BaseTestWithoutLogIn


class LoginTest(BaseTestWithoutLogIn):
    def test_positive_login(self):
        self.driver.get(urlSignInPage)
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field(userWithValidData.userName)
        logInPageObj.click_to_continue_button()
        logInPageObj.get_signin_button_text()
        logInPageObj.fill_password_field(userWithValidData.password)
        sleep(6)  # Here we put sleep so as not to be perceived as a robot
        self.assertEqual(logInPageObj.get_signin_button_text(), "Sign in", "ERROR: Wrong 'Sign in' button text")

        logInPageObj.click_to_sign_in_button()
        sleep(10)
        self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title, "You could not signed in successfully ")

    def test_negative_login_with_invalid_password(self):
        self.driver.get(urlSignInPage)
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field(userWithInvalidPassword.userName)
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_field(userWithInvalidPassword.password)
        sleep(10)  # Here we put sleep so as not to be perceived as a robot
        logInPageObj.click_to_sign_in_button()
        sleep(5)
        self.assertTrue(logInPageObj.is_wrong_password_error_message_appear(), "Error: Should see a message about incorrect password but it did not show")

    def test_negative_login_with_invalid_login(self):
        self.driver.get(urlSignInPage)
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field(userWithInvalidUsername.userName)
        logInPageObj.click_to_continue_button()
        self.assertTrue(logInPageObj.is_wrong_username_error_message_appear(), "Error: Should see a message about incorrect email address/mobile but it did not show")


