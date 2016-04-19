#base.py
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# ++++selenium-server -p 4444
"""
    To run the functional tests
    Useful Commands Updated
        python3 manage.py test functional_tests
    To run the unit tests
        python3 manage.py test lists
 """
class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_host = arg.split('=')[1]
                cls.server_url = 'http://' + cls.server_host
                cls.against_staging = True
                return
        super().setUpClass()
        cls.against_staging = False
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if not cls.against_staging:
            super().tearDownClass()
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
