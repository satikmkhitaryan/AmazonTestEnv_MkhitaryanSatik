from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.navigationBar_.changeLanguageAndCurrencySettingsPage import ChangeLanguageAndCurrencySettingsPage
from tests_.baseTest import BaseTestWithLogIn


class ChangeLanguage(BaseTestWithLogIn):
    def test_change_language_from_navigation_bar(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_espanol_icon()
        self.assertTrue(navigationBarObj.validate_language_icon_text("ES"), "Language should be espanol but is not")

    def test_change_language_from_language_settings_page(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_change_language_icon()
        changeLanguageObj = ChangeLanguageAndCurrencySettingsPage(self.driver)
        changeLanguageObj.click_to_english_language_button()
        changeLanguageObj.click_to_save_changes_button()
        self.assertTrue(navigationBarObj.validate_language_icon_text("EN"), "Language should be english but is not")


