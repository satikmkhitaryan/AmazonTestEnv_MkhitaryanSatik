from selenium import webdriver
from pages_.loginPage import LogInPage
from pages_.navigationBar import NavigationBar
from pages_.searchResultsPage import SearchResultsPage
from pages_.productDetailsPage import ProductDetailsPage
from testData_ import testData
import unittest
from time import sleep


class product_addition_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(testData.urlSignIn)

        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field(testData.loginDataValid["username"])
        logInPageObj.validate_continue_button_text()
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_field(testData.loginDataValid["password"])
        sleep(10)# Here we put sleep so as not to be perceived as a robot
        logInPageObj.click_to_sign_in_button()
        self.navigationBarObj = NavigationBar(self.driver)
        self.navigationBarObj.fill_search_field("laptop")
        self.navigationBarObj.click_to_search_button()
        searchResultsPageObj = SearchResultsPage(self.driver)
        searchResultsPageObj.click_to_first_product()

    def test_add_product_to_cart(self):
        productDetailsPageObj = ProductDetailsPage(self.driver)
        countOfProductsInCartBeforeAddingNewProductToCart = self.navigationBarObj.get_product_count_in_cart()
        productDetailsPageObj.click_to_add_to_cart_button()
        countOfProductsInCartAfterAddingProductToCart = self.navigationBarObj.get_product_count_in_cart()
        self.assertEqual(int(countOfProductsInCartAfterAddingProductToCart), int(countOfProductsInCartBeforeAddingNewProductToCart)+1, "ERROR: Wrong count of product in cart")

    def tearDown(self):
        self.driver.close()
