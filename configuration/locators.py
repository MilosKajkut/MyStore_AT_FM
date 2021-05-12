from selenium.webdriver.common.by import By


class HomePageLocators:
    HOME_PAGE_URL = 'http://automationpractice.com/index.php'

    # home page nav locators
    HOME_PAGE_TITLE_IMAGE = (By.XPATH, '//*[@class ="img-responsive"]')
    HOME_PAGE_PHONE_NUMBER = (By.XPATH, '//*[@class ="shop-phone"]')
    HOME_PAGE_PHONE_NUMBER_ICON = (By.CSS_SELECTOR, '.shop-phone > i:nth-child(1)')
    HOME_PAGE_PHONE_NUMBER_TEXT = (By.CSS_SELECTOR, '.shop-phone > strong')
    HOME_PAGE_PHONE_EXPECTED_NUMBER = '0123-456-789'
    CONTACT_US = (By.XPATH, '//*[@id="contact-link"]')
    CONTACT_US_TEXT = 'Contact us'
    SIGN_IN = (By.XPATH, '//*[@class="header_user_info"]')
    SIGN_IN_TEXT = 'Sign in'

    # home logo locator
    HOME_PAGE_LOGO = (By.XPATH, '//*[@class="logo img-responsive"]')

    # search bar locators
    SEARCH_BAR = (By.XPATH, '//*[@id="search_query_top"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@class="btn btn-default button-search"]')
    SHOPPING_CART = (By.XPATH, '//*[@class ="shopping_cart"]')

    # cart product block locators
    CART_LOCATOR = (By.XPATH, '//*[@class ="shopping_cart"]')
    CART_TEXT_LOCATOR = (By.CSS_SELECTOR, 'div.shopping_cart a b')
    CART_NO_PRODUCT = (By.XPATH, '//*[@class ="ajax_cart_no_product"]')
    CART_QUANTITY = (By.XPATH, '//*[@class ="ajax_cart_quantity"]')
    CART_PRODUCT_TEXT = (By.XPATH, '//*[@class ="ajax_cart_product_txt"]')
    CART_PRODUCTS_TEXT = (By.XPATH, '//*[@class ="ajax_cart_product_txt_s"]')
    CART_BLOCK_LIST = (By.XPATH, '//*[@class="cart_block_list"]')
    CART_PRODUCTS_LIST = (By.XPATH, '//*[@class="products"]')
    CART_FIRST_PRODUCT_IN_LIST = (By.CSS_SELECTOR, 'dt.first_item')
    CART_LAST_PRODUCT_IN_LIST = (By.CSS_SELECTOR, 'dt.last_item')
    CART_PRODUCT_ITEMS_IN_LIST = (By.CSS_SELECTOR, 'dt.item')
    CART_PRODUCTS_INFO = (By.XPATH, '//dl/dt/div')
    CART_SHIPPING = (By.XPATH, '//*[@class="price cart_block_shipping_cost ajax_cart_shipping_cost"]')
    CART_TOTAL_PRICE = (By.XPATH, '//*[@class="cart-prices-line last-line"]')
    CART_CHECK_OUT_BUTTON = (By.XPATH, '//*[@id="button_order_cart"]')

    @staticmethod
    def cart_product_info_title(title):
        """
        Form Web Element locator, locator is for title of product in cart product list.

        :param title:
        Title of Product which will be located.

        :return:
        Tuple of Web Locator.

        """
        assert isinstance(title, str), 'title should be instance of string.'

        return By.XPATH, '//*[@class="cart_block_product_name" and @title ="{}"]'.format(title)

    @staticmethod
    def cart_product_quantity(product_number):
        """
        Form Web Element locator, locator is for quantity of product in cart product list.

        :param product_number:
        Index of Product in Cart Product List.

        :return:
        Tuple of Web Locator.

        """
        assert isinstance(product_number, int), 'product_number should be instance of integer.'
        assert product_number >= 0, 'product_number should be equal or greater than zero.'

        return By.XPATH, '//dl/dt[{}]/div/div/span/span'.format(product_number)

    @staticmethod
    def cart_product_color_size(product_number):
        """
        Form Web Element locator, locator is for size and color of product in cart product list.

        :param product_number:
        Index of Product in Cart Product List.

        :return:
        Tuple of Web Locator.

        """
        assert isinstance(product_number, int), 'product_number should be instance of integer.'
        assert product_number >= 0, 'product_number should be equal or greater than zero.'

        return By.XPATH, '//dl/dt[{}]/div/div[2]'.format(product_number)

    @staticmethod
    def cart_product_price(product_number):
        """
        Form Web Element locator, locator is for price of product in cart product list.

        :param product_number:
        Index of Product in Cart Product List.

        :return:
        Tuple of Web Locator.

        """
        assert isinstance(product_number, int), 'product_number should be instance of integer.'
        assert product_number >= 0, 'product_number should be equal or greater than zero.'

        return By.XPATH, '//dl/dt[{}]/div/span'.format(product_number)

    @staticmethod
    def cart_product_remove_link(product_number):
        """
        Form Web Element locator, locator is for remove link of product in cart product list.

        :param product_number:
        Index of Product in Cart Product List.

        :return:
        Tuple of Web Locator.

        """
        assert isinstance(product_number, int), 'product_number should be instance of integer.'
        assert product_number >= 0, 'product_number should be equal or greater than zero.'

        return By.XPATH, '//dl/dt[{}]/span/a'.format(product_number)

    # main menu
    MAIN_MENU_WOMEN = (By.XPATH, '//*[@class="sf-with-ul" and @title = "Women"]')
    MAIN_MENU_DRESSES = (By.CSS_SELECTOR, '.sf-menu > li:nth-child(2) > a')
    MAIN_MENU_TSHIRTS = (By.CSS_SELECTOR, '.sf-menu > li:nth-child(3) > a:nth-child(1)')
    MAIN_MENU_WOMEN_OPTIONS = (By.XPATH, '//div[6]/ul/li[1]/ul')
    MAIN_MENU_DRESSES_OPTIONS = (By.XPATH, '//div[6]/ul/li[2]/ul')
    MAIN_MENU_HOVER = (By.XPATH, '//li[@class="sfHover"]//*[contains(@class,"submenu-container clearfix first-in-line-xs")]')
    MAIN_MENU_WOMEN_HOVER_TOP = (By.XPATH, '//li[@class="sfHover"]//*[@class="sf-with-ul" and @title="Tops"]')
    MAIN_MENU_WOMEN_HOVER_TOP_TSHIRTS = (By.XPATH, '//li[@class="sfHover" ]//*[@title="T-shirts"]')
    MAIN_MENU_WOMEN_HOVER_TOP_BLOUSES = (By.XPATH, '//li[@class="sfHover" ]//*[@title="Blouses"]')
    MAIN_MENU_WOMEN_HOVER_DRESSES = (By.XPATH, '//li[@class="sfHover"]//*[@class="sf-with-ul" and @title="Dresses"]')
    MAIN_MENU_WOMEN_HOVER_DRESSES_CASUAL_DRESSES = (By.XPATH, '//li[@class="sfHover"]//*[@title="Casual Dresses"]')
    MAIN_MENU_WOMEN_HOVER_DRESSES_EVENING_DRESSES = (By.XPATH, '//li[@class="sfHover" ]//*[@title="Evening Dresses"]')
    MAIN_MENU_WOMEN_HOVER_DRESSES_SUMMER_DRESSES = (By.XPATH, '//li[@class="sfHover" ]//*[@title="Summer Dresses"]')
    MAIN_MENU_DRESSES_CASUAL_DRESSES = (By.XPATH, '//*[@class="sfHover"]//ul[@class="submenu-container clearfix first-in-line-xs"]//*[@title="Casual Dresses"]')
    MAIN_MENU_DRESSES_EVENING_DRESSES = (By.XPATH, '//*[@class="sfHover"]//ul[@class="submenu-container clearfix first-in-line-xs"]//*[@title="Evening Dresses"]')
    MAIN_MENU_DRESSES_SUMMER_DRESSES = (By.XPATH, '//*[@class="sfHover"]//ul[@class="submenu-container clearfix first-in-line-xs"]//*[@title="Summer Dresses"]')
    MAIN_MENU_CATEGORY_NAME = (By.XPATH, '//*[@class ="cat-name"]')
    # home page tabs
    POPULAR_TAB = (By.XPATH, '//*[@id="home-page-tabs"]//a[@class="homefeatured"]')
    POPULAR_TAB_ACTIVE = (By.XPATH, '//li[@class="active"]//a[@class="homefeatured"]')
    POPULAR_TAB_CONTENT = (By.XPATH, '//*[@id="homefeatured"]//div[@class="product-container"][1]//img[@class="replace-2x img-responsive"]')
    BEST_SELLER_TAB = (By.XPATH, '//a[@class="blockbestsellers"]')
    BEST_SELLER_TAB_ACTIVE = (By.XPATH, '//li[@class="active"]//a[@class="blockbestsellers"]')
    BEST_SELLER_TAB_CONTENT = (By.XPATH, '//*[@id="blockbestsellers"]//div[@class="product-container"][1]//img[@class="replace-2x img-responsive"]')

    @staticmethod
    def get_popular_tab_product_by_title(title):
        """
        Form Web Element locator, locator is for title of product in Popular tab in Home Page.

        :param title:
        Title of Product which will be located.

        :return:
        Tuple of Web Locator.

        """
        assert isinstance(title, str), 'title should be instance of string.'

        return By.XPATH, '//*[@id="homefeatured"]//a[@class="product-name" and @title="{}"]'.format(title)

    @staticmethod
    def get_popular_add_button_of_product(product_number):
        """
        Form Web Element locator, locator is for add button for product in Home Page tabs.

        :param product_number:
        Index of Product in Cart Product List.

        :return:
        Tuple of Web Locator.
        """
        assert isinstance(product_number, int), 'product_number should be instance of integer.'
        assert product_number >= 0, 'product_number should be equal or greater than zero.'

        return By.XPATH, '//ul[@class="product_list grid row homefeatured tab-pane active"]//div[@class="button-container"]//a[@title="Add to cart" and @data-id-product="{}"]'.format(product_number)

    @staticmethod
    def get_popular_more_button_of_product(product_number):
        """
        Form Web Element locator, locator is for more button for product in Home Page tabs.

        :param product_number:
        Index of Product in Cart Product List.

        :return:
        Tuple of Web Locator.

        """

        assert isinstance(product_number, int), 'product_number should be instance of integer.'
        assert product_number >= 0, 'product_number should be equal or greater than zero.'

        return By.XPATH, '//div[@class="button-container"]//a[@class="button lnk_view btn btn-default" and contains(@href, "product={}")'.format(product_number)

    @staticmethod
    def get_popular_tab_price_of_product(product_number):
        """
        Form Web Element locator, locator is for price for product in Home Page tabs.

        :param product_number:
        Index of Product in Cart Product List.

        :return:
        Tuple of Web Locator.

        """

        assert isinstance(product_number, int), 'product_number should be instance of integer.'
        assert product_number >= 0, 'product_number should be equal or greater than zero.'

        return By.XPATH, '//ul[1]/li[{}]/div/div[2]/div[1]/span'.format(product_number)


class ContactPageLocators:
    CONTACT_US_URL = 'http://automationpractice.com/index.php?controller=contact'


class SignInLocators:
    SIGN_IN_URL = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'


class SearchLocators:
    SEARCH_NAVIGATOR = (By.XPATH, '//*[@class ="navigation_page"]')
    SEARCH_NAVIGATOR_TEXT = 'Search'


class ShoppingCart:
    YOUR_SHOPPING_CART = (By.XPATH, '//*[@class ="navigation_page"]')
    YOUR_SHOPPING_CART_TEXT = 'Your shopping cart'


class WomenPage:
    WOMEN_PAGE_NAVIGATION = (By.XPATH, '//*[@class ="navigation_page"]')
    WOMEN_PAGE_NAVIGATION_TEXT = 'Women'


class TopPage:
    TOP_NAVIGATION = (By.CSS_SELECTOR, 'span.navigation-pipe:nth-child(4)')
    TOP_NAVIGATION_TEXT = 'Tops'


class DressesPage:
    DRESSES_NAVIGATION = (By.CSS_SELECTOR, 'span.navigation-pipe:nth-child(4)')
    DRESSES_NAVIGATION_TEXT = 'Dresses'


class TShirtPage:
    T_SHIRT_NAVIGATION = (By.CSS_SELECTOR, 'span.navigation-pipe:nth-child(6)')
    T_SHIRT_NAVIGATION_TEXT = 'T-shirts'


class BlousesPage:
    BLOUSES_NAVIGATION = (By.CSS_SELECTOR, 'span.navigation-pipe:nth-child(6)')
    BLOUSES_NAVIGATION_TEXT = 'Blouses'


class CasualDressesPage:
    CASUAL_DRESSES_NAVIGATION = (By.CSS_SELECTOR, 'span.navigation-pipe:nth-child(6)')
    CASUAL_DRESSES_NAVIGATION_TEXT = 'Casual Dresses'


class EveningDressesPage:
    EVENING_DRESSES_NAVIGATION = (By.CSS_SELECTOR, 'span.navigation-pipe:nth-child(6)')
    EVENING_DRESSES_NAVIGATION_TEXT = 'Evening Dresses'


class SummerDressesPage:
    SUMMER_DRESSES_NAVIGATION = (By.CSS_SELECTOR, 'span.navigation-pipe:nth-child(6)')
    SUMMER_DRESSES_NAVIGATION_TEXT = 'Summer Dresses'
