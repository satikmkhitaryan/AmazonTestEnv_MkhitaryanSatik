from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.productRelatedPage_.searchResultsPage import SearchResultsPage
from pages_.productRelatedPage_.productDetailsPage import ProductDetailsPage
from tests_.baseTest import BaseTestWithLogIn
from pages_.navigationBar_.cartPage import CartPage


class ProductAdditionTest(BaseTestWithLogIn):
    def test_validate_product_addition_by_cart_count(self):
        self.navigationBarObj = NavigationBar(self.driver)
        self.navigationBarObj.fill_search_field("laptop")
        self.navigationBarObj.click_to_search_button()
        searchResultsPageObj = SearchResultsPage(self.driver)
        searchResultsPageObj.click_to_first_product()
        productDetailsPageObj = ProductDetailsPage(self.driver)
        countOfProductsInCartBeforeAddingNewProductToCart = self.navigationBarObj.get_product_count_in_cart()
        productDetailsPageObj.click_to_add_to_cart_button()
        countOfProductsInCartAfterAddingProductToCart = self.navigationBarObj.get_product_count_in_cart()
        self.assertEqual(countOfProductsInCartAfterAddingProductToCart, countOfProductsInCartBeforeAddingNewProductToCart + 1, "ERROR: Wrong count of product in cart")

    def test_validate_product_addition_by_message(self):
        self.navigationBarObj = NavigationBar(self.driver)
        self.navigationBarObj.fill_search_field("laptop")
        self.navigationBarObj.click_to_search_button()
        searchResultsPageObj = SearchResultsPage(self.driver)
        searchResultsPageObj.click_to_first_product()
        productDetailsPageObj = ProductDetailsPage(self.driver)
        productDetailsPageObj.click_to_add_to_cart_button()
        cartPageObj = CartPage(self.driver)
        self.assertTrue(cartPageObj.is_added_to_cart_message_appear(), "ERROR: 'Added to cart' message does not appear")