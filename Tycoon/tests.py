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


class MemberModelTest(TestCase):

    def test_saving_and_retrieving_members(self):
        first_member = Member()
        first_member.name = 'Charlie Cook'
        first_member.save()

        second_member = Member()
        second_member.name = 'Vinnie Vinnicombe'
        second_member.save()

        saved_members = Member.objects.all()
        self.assertEqual(saved_members.count(), 2)

        first_saved_member = saved_members[0]
        second_saved_member = saved_members[1]
        self.assertEqual(first_saved_member.name, 'Charlie Cook')
        self.assertEqual(second_saved_member.name, 'Vinnie Vinnicombe')

    def test_saving_and_retrieving_supplies(self):
        first_supply = Supply()
        first_supply.name = 'Teabags'
        first_supply.save()

        second_supply = Supply()
        second_supply.name = 'Coffee'
        second_supply.save()

        saved_supplies = Supply.objects.all()
        self.assertEqual(saved_supplies.count(), 2)

        first_saved_member = saved_supplies[0]
        second_saved_member = saved_supplies[1]
        self.assertEqual(first_saved_member.name, 'Teabags')
        self.assertEqual(second_saved_member.name, 'Coffee')
