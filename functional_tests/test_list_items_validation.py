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
    @skip
    def test_cannot_add_empty_list_items(self):
        pass
