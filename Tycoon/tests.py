from django.core.urlresolvers import resolve
from django.test import TestCase
from tycoon.views import home_page
from tycoon.models import Member, Supply


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
