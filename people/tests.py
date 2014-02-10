from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from people.views import people_page
from people.models import People


class PeoplePageTest(TestCase):

    def test_people_url_resolves_to_people_page_view(self):
        found = resolve('/people/')
        self.assertEqual(found.func, people_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = people_page(request)
        self.assertIn(b'<title>People</title>', response.content)


class PeopleModelTest(TestCase):

    def test_retrieving_people(self):
        first_person = People()
        first_person.first_name = 'Zunayed'
        first_person.last_name = 'Ali'
        first_person.title = 'Dev'
        first_person.save()

        second_person = People()
        second_person.first_name = 'Mike'
        second_person.last_name = 'Dory'
        second_person.title = 'boss'
        second_person.save()

        saved_items = People.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.first_name, 'Zunayed')
        self.assertEqual(first_saved_item.last_name, 'Ali')
        self.assertEqual(first_saved_item.title, 'Dev')

        self.assertEqual(second_saved_item.first_name, 'Mike')
