from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """
    Base Page class represent basic page functionality for all pages on site:
    http://automationpractice.com/index.php

    """

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator, sec_wait=10):
        """
        Method perform left click on Web Element located by Locator.
        Default wait for left click is 10 sec.

        :param sec_wait:
        How many seconds should be wait for left click action.

        :param by_locator:
        Web Element locator represented as tuple of two elements.
        First element - Type of Locator By
        Second element - string of Web Element Locator.

        :return:
        True if left click is performed successfully, False otherwise.

        """
        assert isinstance(by_locator, tuple), 'by_locator should be instance of tuple.'
        assert isinstance(sec_wait, int), 'sec_wait should be instance of integer.'
        assert sec_wait >= 0, 'sec_wait should be equal or greater than 0.'

        try:
            WebDriverWait(self.driver, sec_wait).until(ec.visibility_of_element_located(by_locator)).click()
            return True
        except TimeoutException:
            return False

    def do_send_key(self, by_locator, text, sec_wait=10):
        """
        Method sends text to Web Element located by Locator.
        Default wait for send text action is 10 sec.

        :param text:
        Text which will be sent to Web Element.

        :param sec_wait:
        How many seconds should be wait for send text action.

        :param by_locator:
        Web Element locator represented as tuple of two elements.
        First element - Type of Locator By
        Second element - string of Web Element Locator.

        :return:
        Web Element if send text is preformed successfully, False otherwise.

        """
        assert isinstance(by_locator, tuple), 'by_locator should be instance of tuple.'
        assert isinstance(text, str), 'text should be instance of string.'
        assert isinstance(sec_wait, int), 'sec_wait should be instance of integer.'
        assert sec_wait >= 0, 'sec_wait should be equal or greater than 0.'

        try:
            WebDriverWait(self.driver, sec_wait).until(ec.visibility_of_element_located(by_locator)).send_keys(text)
            return True
        except TimeoutException:
            return False

    def get_element_text(self, by_locator, sec_wait=10):
        """
        Method get text on Web Element located by Locator.
        Default wait for get text action is 10 sec.

        :param sec_wait:
        How many seconds should be wait for get text action.

        :param by_locator:
        Web Element locator represented as tuple of two elements.
        First element - Type of Locator By
        Second element - string of Web Element Locator.

        :return:
        Web Element if get text is performed successfully, False otherwise.

        """
        assert isinstance(by_locator, tuple), 'by_locator should be instance of tuple.'
        assert isinstance(sec_wait, int), 'sec_wait should be instance of integer.'
        assert sec_wait >= 0, 'sec_wait should be equal or greater than 0.'

        try:
            return WebDriverWait(self.driver, sec_wait).until(ec.visibility_of_element_located(by_locator)).text
        except TimeoutException:
            return False

    def is_url_correct(self, expected_url, sec_wait=10):
        """
        Method check is expected URL same as actual URL.

        :param expected_url:
        Expected URL of Page.

        :param sec_wait:
        How many seconds should be wait for get text action.

        :return:
        True if expected URL and actual URL is matching, False otherwise.

        """
        assert isinstance(expected_url, str), 'expected_url should be instance of string.'

        try:
            return WebDriverWait(self.driver, sec_wait).until(ec.url_to_be(expected_url))
        except TimeoutException:
            return False

    def find_all_elements(self, by_locator, sec_wait=10):
        """
        Method find all Web Elements located bu Locator.

        :param sec_wait:
        How many seconds should be wait for get text action.

        :param by_locator:
        Web Element locator represented as tuple of two elements.
        First element - Type of Locator By
        Second element - string of Web Element Locator.

        :return:
        List of Web Elements located by Locator, False otherwise.
        """
        assert isinstance(by_locator, tuple), 'by_locator should be instance of tuple.'
        assert isinstance(sec_wait, int), 'sec_wait should be instance of integer.'
        assert sec_wait >= 0, 'sec_wait should be equal or greater than 0.'

        try:
            return WebDriverWait(self.driver, sec_wait).until(ec.visibility_of_all_elements_located(by_locator))
        except TimeoutException:
            return False

    def is_element_visible(self, by_locator, sec_wait=10):
        """
        Method check is element visible or not.

        :param sec_wait:
        How many seconds should be wait for visible.

        :param by_locator:
        Web Element locator represented as tuple of two elements.
        First element - Type of Locator By
        Second element - string of Web Element Locator..

        :return:
        Element if located element is visible, False otherwise
        """
        assert isinstance(by_locator, tuple), 'by_locator should be instance of tuple.'
        assert isinstance(sec_wait, int), 'sec_wait should be instance of integer.'
        assert sec_wait >= 0, 'sec_wait should be equal or greater than 0.'

        try:
            element = WebDriverWait(self.driver, sec_wait).until(ec.visibility_of_element_located(by_locator))
            return element
        except TimeoutException:
            return False

    def is_clickable(self, by_locator, sec_wait=10):
        """
        Method check is element clickable or not.

        :param sec_wait:
        How many seconds should be wait clickable.

        :param by_locator:
        Web Element locator represented as tuple of two elements.
        First element - Type of Locator By
        Second element - string of Web Element Locator.

        :return:
        Element if located element is clickable, False otherwise
        """
        assert isinstance(by_locator, tuple), 'by_locator should be instance of tuple.'

        try:
            return WebDriverWait(self.driver, sec_wait).until(ec.element_to_be_clickable(by_locator))
        except TimeoutException:
            return False

    def is_text_of_element_correct(self, by_locator, expected_text):
        """
        Method check is Web Element text same as expected text.

        :param by_locator:
        Web Element locator represented as tuple of two elements.
        First element - Type of Locator By
        Second element - string of Web Element Locator.

        :param expected_text:
        Text which is expected to be in Web Element text.

        :return:
        True if Web Element text is same as expected text, False otherwise.

        """
        assert isinstance(expected_text, str), 'expected_text should be type str'
        assert isinstance(by_locator, tuple), 'by_locator should be instance of tuple.'

        element = self.is_element_visible(by_locator)
        if element:
            return element.text == expected_text
        else:
            return False

    def move_cursor_to_element(self, by_locator):
        """
        Method move cursor to Web Element located by by_locator parameter.

        :param by_locator:
        Web Element locator represented as tuple of two elements.
        First element - Type of Locator By
        Second element - string of Web Element Locator

        :return:
        False if cursor is not moved to Web Element, True otherwise.
        """
        assert isinstance(by_locator, tuple), 'by_locator should be instance of tuple.'

        element = self.is_element_visible(by_locator)
        if element:
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            return True
        else:
            return False

