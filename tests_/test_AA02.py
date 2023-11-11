from selenium import webdriver
from pages_.loginPage import LogInPage
from pages_.navigationBar import NavigationBar
from pages_.searchResultsPage import SearchResultsPage
from pages_.productDetailsPage import ProductDetailsPage
import unittest
from time import sleep


class AA_02(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field("huy.ev.apaga.hk@gmail.com")
        logInPageObj.validate_continue_button_text()
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_field("Amazon@Selenium@2023")
        # Here we put sleep so as not to be perceived as a robot
        sleep(10)
        logInPageObj.click_to_sign_in_button()
        self.navigationBarObj = NavigationBar(self.driver)
        self.navigationBarObj.fill_search_field("bookshelf")
        self.navigationBarObj.click_to_search_button()
        searchResultsPageObj = SearchResultsPage(self.driver)
        searchResultsPageObj.click_to_first_product()

    def test_products_count_in_cart(self):
        productDetailsPageObj = ProductDetailsPage(self.driver)
        countOfProductsInCartBeforeAdding = self.navigationBarObj.validate_count_of_products_in_cart()
        productDetailsPageObj.click_to_add_to_cart_button()
        countOfProductsInCartAfterAdding = self.navigationBarObj.validate_count_of_products_in_cart()
        if int(countOfProductsInCartAfterAdding) != int(countOfProductsInCartBeforeAdding) + 1:
            print("ERROR: Wrong count of product in cart")
            exit(4)

    def tearDown(self):
        self.driver.close()
