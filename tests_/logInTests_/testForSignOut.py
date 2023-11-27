from tests_.baseTest import BaseTestWithLogIn
from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.logInPage_.loginPage import LogInPage

class SignOutTest(BaseTestWithLogIn):
    def test_for_sign_out(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.move_to_account_and_lists_button()
        navigationBarObj.click_to_sign_out_button()

        loginPageObj = LogInPage(self.driver)
        self.assertTrue(loginPageObj.is_sign_in_text_appear(), "You could not sign out from Amazon.com")

