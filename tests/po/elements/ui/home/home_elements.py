"""
Home Elements
"""

from tests import config
from tests.po.elements.async_elements import AsyncElement
from tests.po.elements.base_elements import ElementCollection


class HomeElements(ElementCollection):
    """
    Base class for HomeElements
    """

    def __init__(self):
        """
        Initalise variables
        """
        search_field_text = config.SEARCH_TEXT_KEY
        button_field_text = config.SEARCH_BUTTON_KEY
        
        self.search_text = AsyncElement(search_field_text)
        self.search_button = AsyncElement(button_field_text)
