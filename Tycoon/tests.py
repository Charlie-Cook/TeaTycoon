from django.core.urlresolvers import resolve
from django.test import TestCase
from tycoon.views import home_page
from tycoon.models import Member, Supply, Collection, Coffers
import datetime as dt


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
        Collection.objects.create(amount=2.00, date=dt.datetime.today().strftime('%Y-%m-%d'))

    def start_coffers(self):
        Coffers.objects.create(amount=2.00, date=dt.datetime.today().strftime('%Y-%m-%d'))

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
        # todo Update collection view to increase coffers by latest collection amount

    def test_purchasing_supplies(self):
        Supply.objects.create(name='Teabags', stocked=False)
        self.client.get('/supplies/1/purchase')
        supplies = Supply.objects.all()
        new_supply = supplies[0]
        self.assertTrue(new_supply.stocked)

    def test_purchasing_supplies_reduces_coffers(self):
        pass  # todo

    def test_purchase_record_is_updated_when_buying_supply(self):
        pass  # todo

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
        # Line below gets the latest member in the table - this is useful later
        only_member = Member.objects.filter(name='Charlie Cook').order_by('-id')[0]
        self.assertFalse(only_member.paid)

    def test_collection_saves_correctly(self):
        self.client.post(
            '/members/new_collection',
            data={'collection_amount': '2.55'}
        )
        latest_collection = Collection.objects.filter().order_by('-id')[0]
        date_today = dt.datetime.today().strftime('%Y-%m-%d')
        self.assertEqual(date_today, str(latest_collection.date))
        self.assertEqual(2.55, latest_collection.amount)
