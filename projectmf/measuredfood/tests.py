from django.test import TestCase

# Run the unit tests using
# python manage.py test measuredfood.tests


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
