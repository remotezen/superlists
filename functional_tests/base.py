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
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()
