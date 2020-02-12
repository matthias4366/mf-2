import re
import sys
sys.path.append('..')
sys.path.append('...')
sys.path.append('....')
sys.path.append('.....')
sys.path.append('......')
from measuredfood.utils.rawingredient3.make_name_of_duplicate_rawingredient3 \
    import make_name_of_duplicate_rawingredient3
from django.test import TestCase

# Run the unit tests using
# python manage.py test measuredfood.tests


class MakeNameOfDuplicateRawIngredient3Test(TestCase):

    def test_make_name_of_duplicate_rawingredient3_no_initial_numbers(self):
        original_name = "Pasta"
        result_actual = make_name_of_duplicate_rawingredient3(
            original_name,
            re,
        )
        result_expected = "Pasta1"
        self.assertEqual(
            result_actual,
            result_expected
        )

    def test_make_name_of_duplicate_rawingredient3_with_initial_numbers(self):
        original_name = "Pasta1973"
        result_actual = make_name_of_duplicate_rawingredient3(
            original_name,
            re,
        )
        result_expected = "Pasta1974"
        self.assertEqual(
            result_actual,
            result_expected
        )
