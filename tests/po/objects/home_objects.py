"""
Home Objects
"""

from tests.base_page import BasePage
from tests.po.elements.ui.home.home_elements import HomeElements


class HomeObjects(BasePage):
    """
    HomeObjects class which implements BasePage logic and page actions
    """

    def __init__(self, browser):
        """
        Initalise browser instances
        :param browser: webdriver browser to be set
        """
        self.home = HomeElements()
        self.set_browser(browser)

    def open_url(self):
        """
        Opens url
        """
        self.go_to_url()
        self.home.search_button()

    """
    Logic
    """
    def search_key_word(self, key_word):
        """
        Enters key_word parameter into search field and searches key_word
        :param key_word: string to be searched
        """
        self.fill_search_text(key_word)
        self.click_search_button()

    """
    Page Actions
    """
    def fill_search_text(self, value=None):
        """
        Fill in search field with value
        :param: value to pass into fill field
        """
        self.home.search_text.fill_field(value)

    def click_search_button(self):
        """
        Implements search button click
        """
        self.home.search_button.click_field(index=1)
