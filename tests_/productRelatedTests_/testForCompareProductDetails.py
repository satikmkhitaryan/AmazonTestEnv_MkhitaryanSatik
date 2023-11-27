from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.productRelatedPage_.searchResultsPage import SearchResultsPage
from pages_.productRelatedPage_.productDetailsPage import ProductDetailsPage
from tests_.baseTest import BaseTestWithLogIn


class CompareProductDetails(BaseTestWithLogIn):
    def test_validate_product_name_and_price(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("toys for ages 5")
        navigationBarObj.click_to_search_button()
        searchResultsPageObj = SearchResultsPage(self.driver)
        name = searchResultsPageObj.get_first_product_name()
        price = searchResultsPageObj.get_first_product_price()
        searchResultsPageObj.click_to_first_product()
        productDetailsPageObj = ProductDetailsPage(self.driver)
        expectedName = productDetailsPageObj.get_product_name()
        expectedPrice = productDetailsPageObj.get_product_price()
        self.assertEqual(name, expectedName, "ERROR: The products name and expected name don't same")
        self.assertEqual(price, expectedPrice, "ERROR: The products price and expected price don't same")

