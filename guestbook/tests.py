from django.test import TestCase
from guestbook.models import Hit


class HitCounterTestCase(TestCase):
    def test_hit_counter_increments_by_one_when_page_is_hit(self):
        count = Hit.objects.count()
        response = self.client.get('/')

        self.assertEqual(count + 1, response.context['hits'])


class GuestEntryTestCase(TestCase):
    def test_when_a_guest_signs_their_name_is_recorded(self):
        response = self.client.post('/', {'name': 'John Doe'})

        self.assertEqual(response.status_code, 200)

        response = self.client.get('/')
        self.assertIn('John Doe', [entry.name for entry in response.context['entries']])

    def test_duplicate_guest_names_are_not_allowed(self):
        response = self.client.post('/', {'name': 'John Doe'})
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/', {'name': 'John Doe'})
        self.assertFalse(response.context['form'].is_valid())
        self.assertIn('name', response.context['form'].errors)
