#test_items_validation.py
from .base import FunctionalTest

from unittest import skip
# ++++selenium-server -p 4444
"""
    To run the functional tests
    Useful Commands Updated
        python3 manage.py test functional_tests
    To run the unit tests
        python3 manage.py test lists
 """

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        error = self.browser.find_element_by_css_selector('has-error')

        self.assertEqual(error.text, "You can't have an empty list item")

        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('1: Make tea')
