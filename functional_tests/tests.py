from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tycoon.models import Coffers, Supply

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

    def add_new_member(self, name):
        inputbox = self.browser.find_element_by_id('id_new_member')
        inputbox.send_keys(name)
        inputbox.send_keys(Keys.ENTER)

    def add_new_supply(self, name):
        inputbox = self.browser.find_element_by_id('id_new_supply')
        inputbox.send_keys(name)
        inputbox.send_keys(Keys.ENTER)

    def purchase_first_supply(self):
        id_of_supply = Supply.objects.order_by('-id')[0].id
        self.browser.execute_script('$("#purchase_form").attr("action", "supplies/%s/purchase")' % (id_of_supply,))
        purchase_button = self.browser.find_element_by_link_text('Purchase')
        purchase_button.click()
        purchase_cost_input = self.browser.find_element_by_id('id_purchase_amount')
        purchase_cost_input.send_keys('1.00')
        save_purchase_button = self.browser.find_element_by_id('id_submit_purchase')
        save_purchase_button.click()

    def test_adding_new_member(self):
        self.browser.get(self.live_server_url)
        self.add_new_member('Charlie Cook')
        table = self.browser.find_element_by_id('id_members_table')
        self.assertIn('Charlie Cook', table.text)

    def test_collecting_from_member(self):
        self.browser.get(self.live_server_url)
        self.add_new_member('Charlie Cook')
        # id_collect_1 is equal to the ID of the collect button of user 1
        collect_button = self.browser.find_element_by_link_text('Collect')
        collect_button.click()
        table = self.browser.find_element_by_id('id_members_table')
        self.assertIn("Paid", table.text)

    def test_starting_new_collection(self):
        self.browser.get(self.live_server_url)
        self.add_new_member('Charlie Cook')
        collect_button = self.browser.find_element_by_link_text('Collect')
        collect_button.click()
        start_collection_btn = self.browser.find_element_by_id('id_start_collection_btn')
        start_collection_btn.click()
        collection_amount_box = self.browser.find_element_by_id('id_collection_amount')
        collection_amount_box.send_keys('2.00')
        collection_submit_btn = self.browser.find_element_by_id('id_submit_collection')
        collection_submit_btn.click()
        member_table = self.browser.find_element_by_id('id_members_table')
        self.assertIn('Unpaid', member_table.text)

    def test_adding_new_supply(self):
        self.browser.get(self.live_server_url)
        self.add_new_supply('Teabags')
        table = self.browser.find_element_by_id('id_supplies_table')
        self.assertIn('Teabags', table.text)

    def test_purchasing_supplies(self):
        Coffers.objects.create(amount=1.00)
        self.browser.get(self.live_server_url)
        self.add_new_supply('Teabags')
        self.purchase_first_supply()
        table = self.browser.find_element_by_id('id_supplies_table')
        self.assertIn("In Stock", table.text)

    def test_marking_supplies_as_out_of_stock(self):
        Coffers.objects.create(amount=1.00)
        self.browser.get(self.live_server_url)
        self.add_new_supply('Teabags')
        self.purchase_first_supply()
        table = self.browser.find_element_by_id('id_supplies_table')
        self.assertIn('In Stock', table.text)
        depleted_button = self.browser.find_element_by_link_text('Depleted?')
        depleted_button.click()
        table = self.browser.find_element_by_id('id_supplies_table')
        self.assertIn('Out Of Stock', table.text)

    def test_purchasing_supplies_reduces_coffers(self):
        Coffers.objects.create(amount=1.00)
        self.browser.get(self.live_server_url)
        coffers = self.browser.find_element_by_id('coffers_amount')
        before_coffers = coffers.text.replace('£', '')
        self.add_new_supply('Teabags')
        self.purchase_first_supply()
        coffers = self.browser.find_element_by_id('coffers_amount')
        after_coffers = coffers.text.replace('£', '')
        self.assertLess(float(after_coffers), float(before_coffers))
        self.assertEqual(float(after_coffers), 0.0)
