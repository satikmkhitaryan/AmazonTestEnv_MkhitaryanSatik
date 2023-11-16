from selenium import webdriver
from pages_.loginPage import LogInPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage
from testData_ import testData
import unittest
from common_.utilities_.customLogger import *
from time import sleep


class delete_product_from_cart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        logInPageObj = LogInPage(self.driver)
        logInPageObj.fill_username_field(testData.loginDataValid["username"])
        logInPageObj.validate_continue_button_text()
        logInPageObj.click_to_continue_button()
        logInPageObj.fill_password_field(testData.loginDataValid["password"])
        sleep(10) # Here we put sleep so as not to be perceived as a robot
        logInPageObj.click_to_sign_in_button()
        self.navigationBarObj = NavigationBar(self.driver)

    def test_validate_emptiness_of_cart(self):
        productCountInCart = self.navigationBarObj.get_product_count_in_cart()
        if int(productCountInCart) == 0:
            logger("WARNING", "Your cart is empty")
        else:
            logger("WARNING", "Yor cart isn't empty")

    def test_delete_first_product_from_cart(self):
        countOfProductsInCartBeforeProductDeleting = self.navigationBarObj.get_product_count_in_cart()
        if int(countOfProductsInCartBeforeProductDeleting) == 0:
            logger("WARNING", "Your Amazon cart is empty. You cannot delete product from cart")
        else:
            self.navigationBarObj.click_to_cart_button()
            cartPageObj = CartPage(self.driver)
            cartPageObj.delete_first_product_from_cart()

    def test_delete_all_products_from_cart(self):
        self.navigationBarObj.click_to_cart_button()
        countOfProductsInCartBeforeAllProductDeleting = self.navigationBarObj.get_product_count_in_cart()
        cartPageObj = CartPage(self.driver)
        if int(countOfProductsInCartBeforeAllProductDeleting) != 0:
            cartPageObj.delete_all_products_from_cart(int(countOfProductsInCartBeforeAllProductDeleting))
        countOfProductsInCartAfterAllProductDeleting = self.navigationBarObj.get_product_count_in_cart()
        self.assertEqual(int(countOfProductsInCartAfterAllProductDeleting), 0, "All products successfully removed from cart")
    def tearDown(self):
        self.driver.close()
