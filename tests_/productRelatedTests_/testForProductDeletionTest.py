from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.navigationBar_.cartPage import CartPage
from pages_.productRelatedPage_.searchResultsPage import SearchResultsPage
from pages_.productRelatedPage_.productDetailsPage import ProductDetailsPage
from tests_.baseTest import BaseTestWithLogIn


class DeleteProductFromCart(BaseTestWithLogIn):
    def test_for_emptiness_of_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        productCountInCart = navigationBarObj.get_product_count_in_cart()
        navigationBarObj.click_to_cart_button()
        cartPageObj = CartPage(self.driver)
        if productCountInCart != 0:
            cartPageObj.delete_all_products_from_cart()
        cartPageObj.is_Amazon_cart_is_empty_message_appear()
    def test_delete_first_product_from_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        if navigationBarObj.get_product_count_in_cart() == 0:
            navigationBarObj.fill_search_field("gravy boat")
            navigationBarObj.click_to_search_button()
            searchResultPageObj = SearchResultsPage(self.driver)
            searchResultPageObj.click_to_first_product()
            productDetailsPageObj = ProductDetailsPage(self.driver)
            productDetailsPageObj.click_to_add_to_cart_button()
        countOfProductsInCartBeforeProductDeleting = navigationBarObj.get_product_count_in_cart()
        navigationBarObj.click_to_cart_button()
        cartPageObj = CartPage(self.driver)
        firstProductCountInCart = cartPageObj.get_first_product_count()
        cartPageObj.delete_first_product_from_cart()
        countOfProductsInCartAfterProductDeleting = navigationBarObj.get_product_count_in_cart()
        self.assertEqual(countOfProductsInCartBeforeProductDeleting, countOfProductsInCartAfterProductDeleting + firstProductCountInCart, "ERROR: Wrong count of product in cart")

    def test_delete_all_products_from_cart(self):
        navigationBarObj = NavigationBar(self.driver)
        if navigationBarObj.get_product_count_in_cart() == 0:
            navigationBarObj.fill_search_field("gravy boat")
            navigationBarObj.click_to_search_button()
            searchResultPageObj = SearchResultsPage(self.driver)
            searchResultPageObj.click_to_first_product()
            productDetailsPageObj = ProductDetailsPage(self.driver)
            productDetailsPageObj.click_to_add_to_cart_button()
        navigationBarObj.click_to_cart_button()
        cartPageObj = CartPage(self.driver)
        cartPageObj.delete_all_products_from_cart()
        countOfProductsInCartAfterAllProductDeleting = navigationBarObj.get_product_count_in_cart()
        self.assertEqual(countOfProductsInCartAfterAllProductDeleting, 0, "All products should be removed but  were not removed")


