# -*- coding: utf-8 -*-
from selenium.webdriver.firefox import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.WebDriver()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    #self.live_server_level states the hosta url,  reverse gives you the relative url of the namespace

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    #this functions test to see whether the "TaskBuster" is the  title of the home page
    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)

    #this function test whether h1( headiing) has the specified color
    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"), "rgba(200, 50, 255, 1)")

    #the if__name__ == '__main__' removed becasue functional_test is a package that will run with the Djano test runner
