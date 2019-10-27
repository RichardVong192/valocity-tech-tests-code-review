"""
Base Selenium
"""

import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tests import config


class SeleniumWebDriver(object):
    """
    Implements class instances and variables initalisation
    """
    
    def __new__(cls):
        """
        Create class instances
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(SeleniumWebDriver, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        """
        Initalise variables
        """
        options = Options()
        self.profile = webdriver.FirefoxProfile()
        self.browser = webdriver.Firefox(options=options)


class SeleniumCase(unittest.TestCase):
    """
    Base Selenium Class
    """
    browser = None
    base_url = config.TEST_ADDRESS
    automation_bug_list = []

    @classmethod
    def setUpClass(cls):
        """
        Set up class instance
        """
        super(SeleniumCase, cls).setUpClass()
        cls.browser = SeleniumWebDriver().browser

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class instance
        """
        cls.browser.quit()
        super(SeleniumCase, cls).tearDownClass()
