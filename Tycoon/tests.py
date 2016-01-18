from django.core.urlresolvers import resolve
from django.test import TestCase
from tycoon.views import home_page
from tycoon.models import Member, Supply, Collection, Coffers, SupplyRecord
import tycoon.helpers as helper


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home_page.html')

    def test_home_page_can_save_a_new_member(self):
        self.client.post(
            '/members/add_member',
            data={'member_text': 'Charlie Cook'}
        )

        self.assertEqual(Member.objects.count(), 1)

    def test_home_page_can_save_a_new_supply(self):
        self.client.post(
            '/supplies/add_supply',
            data={'supply_text': 'Teabags'}
        )

        self.assertEqual(Supply.objects.count(), 1)

    def test_redirects_after_member_POST(self):
        response = self.client.post(
            '/members/add_member',
            data={'member_text': 'Charlie Cook'}
        )
        self.assertRedirects(response, '/')

    def test_redirects_after_supply_POST(self):
        response = self.client.post(
            '/supplies/add_supply',
            data={'supply_text': 'Teabags'}
        )
        self.assertRedirects(response, '/')


class ModelTest(TestCase):
    def create_collection(self):
        Collection.objects.create(amount=2.00)

    def start_coffers(self):
        Coffers.objects.create(amount=2.00)

    def test_saving_and_retrieving_members(self):
        Member.objects.create(name='Charlie Cook')
        Member.objects.create(name='Vinnie Vinnicombe')

        saved_members = Member.objects.all()
        self.assertEqual(saved_members.count(), 2)

        self.assertEqual(saved_members[0].name, 'Charlie Cook')
        self.assertEqual(saved_members[1].name, 'Vinnie Vinnicombe')

    def test_saving_and_retrieving_supplies(self):
        Supply.objects.create(name='Teabags')
        Supply.objects.create(name='Coffee')

        saved_supplies = Supply.objects.all()
        self.assertEqual(saved_supplies.count(), 2)

        self.assertEqual(saved_supplies[0].name, 'Teabags')
        self.assertEqual(saved_supplies[1].name, 'Coffee')

    def test_collection_from_member_changes_status(self):
        self.create_collection()
        self.start_coffers()
        Member.objects.create(name='Charlie Cook', paid=False)
        self.client.get('/members/1/collect')
        members = Member.objects.all()
        debtor = members[0]
        self.assertTrue(debtor.paid)

    def test_collecting_from_member_increases_coffers(self):
        self.start_coffers()
        self.create_collection()
        Member.objects.create(name='Charlie Cook', paid=False)
        self.client.get('/members/1/collect')

    def test_purchasing_supplies(self):
        Supply.objects.create(name='Teabags', stocked=False)
        self.client.post(
            '/supplies/1/purchase',
            data={'purchase_amount': '0.50'}
        )
        supplies = Supply.objects.all()
        new_supply = supplies[0]
        self.assertTrue(new_supply.stocked)

    def test_purchasing_supplies_reduces_coffers(self):
        Coffers.objects.create(amount=1.00)
        Supply.objects.create(name='Teabags', stocked=False)
        before_coffers = helper.get_latest_coffers_amount()
        self.client.post(
            '/supplies/1/purchase',
            data={'purchase_amount': '0.50'}
        )
        after_coffers = helper.get_latest_coffers_amount()
        self.assertLess(after_coffers, before_coffers)
        self.assertEqual(after_coffers, 0.5)

    def test_purchase_record_is_updated_when_buying_supply(self):
        Supply.objects.create(name='Teabags', stocked=False)
        self.client.post(
            '/supplies/1/purchase',
            data={'purchase_amount': '1.00'}
        )
        record_of_supplies = SupplyRecord.objects.all()
        self.assertEqual(record_of_supplies[0].name, 'Teabags')
        self.assertEqual(str(record_of_supplies[0].date), helper.get_current_date())
        self.assertEqual(record_of_supplies[0].cost, 1.00)

    def test_collection_record_is_updated_when_new_collection_started(self):
        pass #  todo

    def test_member_collection_is_updated_when_a_member_pays(self):
        pass #  todo

    def test_marking_supplies_as_depleted(self):
        Supply.objects.create(name='Teabags', stocked=True)
        self.client.get('/supplies/1/depleted')
        supplies = Supply.objects.all()
        depleted_supply = supplies[0]
        self.assertFalse(depleted_supply.stocked)

    def test_starting_collection_resets_collection_status(self):
        self.create_collection()
        Member.objects.create(name='Charlie Cook', paid=True)
        self.client.post(
            '/members/new_collection',
            data={'collection_amount': '2.00'}
        )
        only_member = Member.objects.all()[0]
        self.assertFalse(only_member.paid)

    def test_collection_saves_correctly(self):
        self.client.post(
            '/members/new_collection',
            data={'collection_amount': '2.55'}
        )
        latest_collection_amount = helper.get_latest_collection_amount()
        latest_collection_date = helper.get_latest_collection_date()
        date_today = helper.get_current_date()
        self.assertEqual(date_today, str(latest_collection_date))
        self.assertEqual(2.55, latest_collection_amount)
