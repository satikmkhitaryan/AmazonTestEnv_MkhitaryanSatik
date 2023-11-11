# from selenium import webdriver
# from pages_.loginPage import LogInPage
# from pages_.cartPage import CartPage
# from pages_.navigationBar import NavigationBar
# from pages_.searchResultsPage import SearchResultsPage
# from pages_.productDetailsPage import ProductDetailsPage
# from time import sleep
# import unittest
#
#
# class AA_04(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.driver.delete_all_cookies()
#         self.driver.maximize_window()
#         self.driver.get(
#             "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
#         logInPageObj = LogInPage(self.driver)
#         logInPageObj.fill_username_field("huy.ev.apaga.hk@gmail.com")
#         logInPageObj.validate_continue_button_text()
#         logInPageObj.click_to_continue_button()
#         logInPageObj.fill_password_field("Amazon@Selenium@2023")
#         # Here we put sleep so as not to be perceived as a robot
#         sleep(10)
#         logInPageObj.click_to_sign_in_button()
#
#     def test_delete_product_from_cart(self):
#         self.navigationBarObj = NavigationBar(self.driver)
#         self.navigationBarObj.click_to_cart_button()
#         cartPageObj = CartPage(self.driver)
#         cartPageObj.click_to_save_for_later_for_first_product_button()
#         cartPageObj.delete_first_product_from_cart()
#

    # def test_add_product_to_cart(self):
        #self.navigationBarObj.fill_search_field("bookshelf")
        #self.navigationBarObj.click_to_search_button()
        #searchResultsPageObj = SearchResultsPage(self.driver)
        #searchResultsPageObj.click_to_first_product()
        #productDetailsPageObj = ProductDetailsPage(self.driver)
        #productDetailsPageObj.click_to_add_to_cart_button()

    # def tearDown(self):
    #     self.driver.close()
