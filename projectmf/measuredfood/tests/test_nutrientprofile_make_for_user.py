import sys
sys.path.append('..')
sys.path.append('...')
sys.path.append('....')
sys.path.append('.....')
sys.path.append('......')
from django.test import TestCase

# Run the unit tests using
# python manage.py test measuredfood.tests

from measuredfood.utils.nutrient_profile.nutrientprofile_make_for_user import \
    nutrientprofile_make_for_user


class NutrientProfileMakeForUserTest(TestCase):

    def test_nutrientprofile_make_for_user(self):
        nutrientprofile_result = nutrientprofile_make_for_user(
        )
        self.assertEqual('correct', nutrientprofile_result)
