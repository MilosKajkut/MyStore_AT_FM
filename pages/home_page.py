from pages.base_page import BasePage
from configuration.locators import HomePageLocators, SearchLocators


class HomePage(BasePage):
    """
    Class HomePage provide methods for interacting with Home Page on location:http://automationpractice.com/index.php

    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(HomePageLocators.HOME_PAGE_URL)

    def check_homepage_title_image(self):
        """
        Method check is Home Page Title image exist.

        :return:
        Web Element of Image if image exist, False otherwise.
        """
        return self.is_element_visible(HomePageLocators.HOME_PAGE_TITLE_IMAGE)

    def check_company_phone_number(self):
        """
        Method check is phone number and phone icon are presented on Home Page.

        :return:
        True if Phone icon and Phone number are presented on Home Page. False otherwise.
        """
        if self.is_element_visible(HomePageLocators.HOME_PAGE_PHONE_NUMBER):
            return self.is_element_visible(HomePageLocators.HOME_PAGE_PHONE_NUMBER_ICON) \
                   and self.is_text_of_element_correct(HomePageLocators.HOME_PAGE_PHONE_NUMBER_TEXT, HomePageLocators.HOME_PAGE_PHONE_EXPECTED_NUMBER)
        else:
            return False

    def click_contact_us(self):
        """
        Method perform lef click on Contact Us options on Home Page.

        :return:
        None
        """
        element = self.is_clickable(HomePageLocators.CONTACT_US)
        if element:
            element.click()

    def click_sing_in(self):
        """
        Method perform lef click on Sign In options on Home Page.

        :return:
        None
        """
        element = self.is_clickable(HomePageLocators.SIGN_IN)
        if element:
            element.click()

    def check_contact_us_text(self):
        """
        Method check is Contact Us button text same as expected.

        :return:
        True if Contact Us button text is same as expected text, False otherwise.
        """
        return self.is_text_of_element_correct(HomePageLocators.CONTACT_US, HomePageLocators.CONTACT_US_TEXT)

    def check_sign_in_text(self):
        """
        Method check is Sign In button text same as expected.

        :return:
        True if Sign In button text is same as expected text, False otherwise.
        """
        return self.is_text_of_element_correct(HomePageLocators.SIGN_IN, HomePageLocators.SIGN_IN_TEXT)

    def check_home_page_logo(self, click=False):
        """
        Method perform left click on Home Page Logo if click parameter is True.
        If click parameter is False, check is element visible.

        :param click:
        Bool value which is used to determine what action method should perform.

        :return:
        False if element is not clickable and click is True.
        If click is False, True if element is visible and False otherwise.
        """
        if click:
            element = self.is_clickable(HomePageLocators.HOME_PAGE_LOGO)
            if element:
                element.click()
            else:
                return False
        else:
            return self.is_element_visible(HomePageLocators.HOME_PAGE_LOGO)

    def type_in_search_bar(self, text):
        """
        Method send text to search bar and perform search on Home Page.

        :param text:
        Text which will be sent to Web Element.

        :return:
        True if text is successfully parsed to search bar and clicked, False otherwise.
        """
        assert isinstance(text, str), 'text should be string type.'
        if self.do_send_key(HomePageLocators.SEARCH_BAR, text) and self.do_click(HomePageLocators.SEARCH_BUTTON):
            return self.is_text_of_element_correct(SearchLocators.SEARCH_NAVIGATOR, SearchLocators.SEARCH_NAVIGATOR_TEXT)
        else:
            return False

    def move_cursor_to_cart(self):
        """
        Method move cursor to Cart on Home Page.

        :return:
        True if text is successfully parsed to search bar and clicked, False otherwise.
        """
        return self.move_cursor_to_element(HomePageLocators.CART_LOCATOR)

    



