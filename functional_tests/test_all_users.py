# -*- coding: utf-8 -*-
from selenium.webdriver.firefox import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate
from datetime import date
from django.utils import formats



class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.WebDriver()
        self.browser.implicitly_wait(3)
        activate('en')

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


    def test_home_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)

    def test_localization(self):
        today = date.today()
        for lang in ['es', 'en']:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            local_date = self.browser.find_element_by_id("local-date")
            non_local_date = self.browser.find_element_by_id("non-local-date")
            self.assertEqual(formats.date_format(today, use_l10n=True), local_date.text)
            self.assertEqual(today.strftime('%Y-%m-%d'), non_local_date.text)

    def test_time_zone(self):
        self.browser.get(self.get_full_url("home"))
        tz = self.browser.find_element_by_id("time-tz")
        utc = self.browser.find_element_by_id("time-utc")
        acc = self.browser.find_element_by_id("time-acc")
        self.assertNotEqual(tz, utc)
        self.assertNotIn(acc,[tz, utc] )