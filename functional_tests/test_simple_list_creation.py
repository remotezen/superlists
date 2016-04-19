from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from unittest import skip
# ++++selenium-server -p 4444
"""
    To run the functional tests
    Useful Commands Updated
        python3 manage.py test functional_tests
    To run the unit tests
        python3 manage.py test lists
 """


class NewVisitorTest(FunctionalTest):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # opens browser to check out home page"""
        self.browser.get(self.live_server_url)
        response = self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(3)
        # notices title To-Do in header and title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(u'\ue007')
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers')
        inputbox.send_keys(u'\ue007')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers')
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Use peacock feathers', page_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        self.fail('Finish the test!')
