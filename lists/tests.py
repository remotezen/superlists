from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.shortcuts import render

# First test no even a url in home_page = None
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
