from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

# ++++selenium-server -p 4444


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.close()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # opens browser to check out home page"""
        self.browser.get('http://localhost:8000')
        # notices title To-Do in header and title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
