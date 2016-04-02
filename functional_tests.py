from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string
# ++++selenium-server -p 4444


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.close()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # opens browser to check out home page"""
        self.browser.get('http://localhost:8000')
        # notices title To-Do in header and title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')
        inputbox.send_keys('1: Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        inputbox.send_keys('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly'
        )

        self.fail('Finish the test!')

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.POST['items_text'] = 'A new list item'
        if request.method == 'POST':
            request.POST['item_text'] = 'A new list item'
        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
         'home.html',
             {'new_item_text': 'A new list item'}
         )

if __name__ == '__main__':
    unittest.main(warnings='ignore')
