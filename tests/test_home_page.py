import time

from tests.test_base import BaseTest
from pages.home_page import HomePage
from configuration.locators import *


class TestHomePage(BaseTest):
    # def test_homepage_title_image(self):
    #     home_page = HomePage(self.driver)
    #     assert home_page.check_homepage_title_image()
    #
    # def test_check_company_phone_number(self):
    #     home_page = HomePage(self.driver)
    #     assert home_page.check_company_phone_number()
    #
    # def test_contact_us_homepage(self):
    #     home_page = HomePage(self.driver)
    #     home_page.click_contact_us()
    #     assert home_page.check_contact_us_text()
    #     assert home_page.is_url_correct(ContactPageLocators.CONTACT_US_URL)
    #     home_page.check_home_page_logo(click=True)
    #
    # def test_sign_in_homepage(self):
    #     home_page = HomePage(self.driver)
    #     home_page.click_sing_in()
    #     assert home_page.check_sign_in_text()
    #     assert home_page.is_url_correct(SignInLocators.SIGN_IN_URL)
    #     home_page.check_home_page_logo(click=True)
    #
    # def test_type_text_in_search_bar(self):
    #     home_page = HomePage(self.driver)
    #     assert home_page.type_in_search_bar(text='Faded')
    #
    # def test_cart_text(self):
    #     home_page = HomePage(self.driver)
    #     assert home_page.is_text_of_element_correct(HomePageLocators.CART_NO_PRODUCT, '(empty)')
    #
    # def test_shopping_cart_from_homepage(self):
    #     home_page = HomePage(self.driver)
    #     home_page.do_click(HomePageLocators.CART_TEXT_LOCATOR)
    #     assert home_page.is_text_of_element_correct(ShoppingCart.YOUR_SHOPPING_CART, ShoppingCart.YOUR_SHOPPING_CART_TEXT)
    #
    # def test_go_to_women_page_from_homepage(self):
    #     home_page = HomePage(self.driver)
    #     home_page.do_click(HomePageLocators.MAIN_MENU_WOMEN)
    #     assert home_page.is_text_of_element_correct(WomenPage.WOMEN_PAGE_NAVIGATION, WomenPage.WOMEN_PAGE_NAVIGATION_TEXT)
    #
    # def test_open_top_women_menu_on_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.move_cursor_to_element(HomePageLocators.MAIN_MENU_WOMEN):
    #         if home_page.do_click(HomePageLocators.MAIN_MENU_WOMEN_HOVER_TOP):
    #             assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, TopPage.TOP_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_open_t_shirt_women_menu_on_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.move_cursor_to_element(HomePageLocators.MAIN_MENU_WOMEN):
    #         if home_page.do_click(HomePageLocators.MAIN_MENU_WOMEN_HOVER_TOP_TSHIRTS):
    #             assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, TShirtPage.T_SHIRT_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_open_blouses_women_menu_on_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.move_cursor_to_element(HomePageLocators.MAIN_MENU_WOMEN):
    #         if home_page.do_click(HomePageLocators.MAIN_MENU_WOMEN_HOVER_TOP_BLOUSES):
    #             assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, BlousesPage.BLOUSES_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_open_dresses_women_menu_on_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.move_cursor_to_element(HomePageLocators.MAIN_MENU_WOMEN):
    #         if home_page.do_click(HomePageLocators.MAIN_MENU_WOMEN_HOVER_DRESSES):
    #             assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, DressesPage.DRESSES_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_open_casual_dresses_women_menu_on_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.move_cursor_to_element(HomePageLocators.MAIN_MENU_WOMEN):
    #         if home_page.do_click(HomePageLocators.MAIN_MENU_WOMEN_HOVER_DRESSES_CASUAL_DRESSES):
    #             assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, CasualDressesPage.CASUAL_DRESSES_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_open_evening_dresses_women_menu_on_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.move_cursor_to_element(HomePageLocators.MAIN_MENU_WOMEN):
    #         if home_page.do_click(HomePageLocators.MAIN_MENU_WOMEN_HOVER_DRESSES_EVENING_DRESSES):
    #             assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, EveningDressesPage.EVENING_DRESSES_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_open_evening_summer_women_menu_on_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.move_cursor_to_element(HomePageLocators.MAIN_MENU_WOMEN):
    #         if home_page.do_click(HomePageLocators.MAIN_MENU_WOMEN_HOVER_DRESSES_SUMMER_DRESSES):
    #             assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, SummerDressesPage.SUMMER_DRESSES_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_go_to_dresses_page_from_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.do_click(HomePageLocators.MAIN_MENU_DRESSES):
    #         assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, DressesPage.DRESSES_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_open_casual_dresses_dresses_menu_on_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.move_cursor_to_element(HomePageLocators.MAIN_MENU_DRESSES):
    #         if home_page.do_click(HomePageLocators.MAIN_MENU_DRESSES_CASUAL_DRESSES):
    #             assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, CasualDressesPage.CASUAL_DRESSES_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_open_evening_dresses_dresses_menu_on_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.move_cursor_to_element(HomePageLocators.MAIN_MENU_DRESSES):
    #         if home_page.do_click(HomePageLocators.MAIN_MENU_DRESSES_EVENING_DRESSES):
    #             assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, EveningDressesPage.EVENING_DRESSES_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_open_summer_dresses_dresses_menu_on_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.move_cursor_to_element(HomePageLocators.MAIN_MENU_DRESSES):
    #         if home_page.do_click(HomePageLocators.MAIN_MENU_DRESSES_SUMMER_DRESSES):
    #             assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, SummerDressesPage.SUMMER_DRESSES_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False
    #
    # def test_go_to_t_shirt_page_from_homepage(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.do_click(HomePageLocators.MAIN_MENU_TSHIRTS):
    #         assert home_page.is_text_of_element_correct(HomePageLocators.MAIN_MENU_CATEGORY_NAME, TShirtPage.T_SHIRT_NAVIGATION_TEXT.upper() + ' ')
    #     else:
    #         assert False

    # def test_select_popular_tab(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.do_click(HomePageLocators.POPULAR_TAB):
    #         assert home_page.is_element_visible(HomePageLocators.POPULAR_TAB_ACTIVE)
    #     else:
    #         assert False
    #
    # def test_select_best_tab(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.do_click(HomePageLocators.BEST_SELLER_TAB):
    #         assert home_page.is_element_visible(HomePageLocators.BEST_SELLER_TAB_ACTIVE)
    #     else:
    #         assert False
    #
    # def test_list_of_popular_items(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.is_element_visible(HomePageLocators.POPULAR_TAB_ACTIVE):
    #         assert home_page.find_all_elements(HomePageLocators.POPULAR_TAB_CONTENT)
    #     else:
    #         home_page.do_click(HomePageLocators.POPULAR_TAB)
    #         if home_page.is_element_visible(HomePageLocators.POPULAR_TAB_ACTIVE):
    #             assert home_page.find_all_elements(HomePageLocators.POPULAR_TAB_CONTENT)
    #         else:
    #             assert False
    #
    # def test_list_of_best_seller_items(self):
    #     home_page = HomePage(self.driver)
    #     if home_page.is_element_visible(HomePageLocators.BEST_SELLER_TAB_ACTIVE):
    #         assert home_page.find_all_elements(HomePageLocators.BEST_SELLER_TAB_CONTENT)
    #     else:
    #         home_page.do_click(HomePageLocators.BEST_SELLER_TAB)
    #         if home_page.is_element_visible(HomePageLocators.BEST_SELLER_TAB_ACTIVE):
    #             assert home_page.find_all_elements(HomePageLocators.BEST_SELLER_TAB_CONTENT)
    #         else:
    #             assert False

    def test_add_first_product_from_popular_tab(self):
        home_page = HomePage(self.driver)
        if home_page.do_click(HomePageLocators.POPULAR_TAB) and home_page.is_element_visible(HomePageLocators.POPULAR_TAB_ACTIVE):
            list_product = home_page.find_all_elements(HomePageLocators.POPULAR_TAB_CONTENT)
            home_page.move_cursor_to_element(HomePageLocators.get_popular_tab_product_by_title(list_product[0].get_attribute('title')))
            assert home_page.do_click(HomePageLocators.get_popular_add_button_of_product(1))
        else:
            assert False

    def test_add_first_product_from_bestseller_tab(self):
        home_page = HomePage(self.driver)
        if home_page.do_click(HomePageLocators.BEST_SELLER_TAB) and home_page.is_element_visible(HomePageLocators.BEST_SELLER_TAB_ACTIVE):
            list_product = home_page.find_all_elements(HomePageLocators.BEST_SELLER_TAB_CONTENT)
            home_page.move_cursor_to_element(HomePageLocators.get_popular_tab_product_by_title(list_product[0].get_attribute('title')))
            assert home_page.do_click(HomePageLocators.get_popular_add_button_of_product(1))
        else:
            assert False
