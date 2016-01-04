from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase


class AdminVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_viewing_the_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Tea Tycoon', self.browser.title)

    def test_adding_new_member(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_member')
        inputbox.send_keys('Charlie Cook')
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_members_table')
        self.assertIn('Charlie Cook', table.text)

    def test_adding_new_supply(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_supply')
        inputbox.send_keys('Teabags')
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_supplies_table')
        self.assertIn('Teabags', table.text)
