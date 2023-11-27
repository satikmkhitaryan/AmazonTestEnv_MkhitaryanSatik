from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.navigationBar_.changeLanguageAndCurrencySettingsPage import ChangeLanguageAndCurrencySettingsPage
from tests_.baseTest import BaseTestWithLogIn


class ChangeCurrencyTest(BaseTestWithLogIn):
    def test_change_currency_settings(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_change_language_icon()
        changeCurrencyObj = ChangeLanguageAndCurrencySettingsPage(self.driver)
        changeCurrencyObj.click_to_select_currency_drop_down_button()
        changeCurrencyObj.click_to_Armenian_Dram_Icon()
        changeCurrencyObj.get_currency_icon_text()
        changeCurrencyObj.click_to_save_changes_button()


