"""
Home Test
"""

import pytest

from test import config
from tests.base_selenium import SeleniumCase
from tests.po.objects.home_objects import HomeObjects


@pytest.mark.readonly
class HomeTest(SeleniumCase):
    """
    HomeTest base class to implement setup and keyword searching
    """

    def setUp(self):
        """
        Setup browser
        """
        self.home = HomeObjects(self.browser)
        self.home.open_url()

    def test_searching_the_key_word(self):
        """
        Test to search keyword
        """
        self.home.search_key_word(config.SEARCHING_KEY)
