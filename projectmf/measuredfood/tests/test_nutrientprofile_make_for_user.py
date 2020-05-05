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
from \
    measuredfood.utils.nutrient_profile\
    .calculate_total_daily_energy_expenditure \
    import calculate_total_daily_energy_expenditure


class NutrientProfileMakeForUserTest(TestCase):

    def test_nutrientprofile_make_for_user(self):
        nutrientprofile_result = nutrientprofile_make_for_user()
        self.assertEqual('correct', nutrientprofile_result)

    def test_calculate_total_daily_energy_expenditure(self):
        """
        The total daily energy expenditure calculation is being tested.
        The formula are copied from https://tdeecalculator.net/.
        Hence, to test whether the results are correct, it is determined
        whether the same results are obtained as are given by
        https://tdeecalculator.net/.
        :return:
        """
        # python manage.py test
        # measuredfood.tests.test_nutrientprofile_make_for_user.NutrientProfileMakeForUserTest.test_calculate_total_daily_energy_expenditure

        # Acceptable difference between the total daily energy expenditure in
        # kcal calculated here and calculated at https://tdeecalculator.net/
        tolerance = 50

        # Case 1:
        value_from_tdee_calculator_dot_net_1 = 1737
        total_daily_energy_expenditure_1 = \
            calculate_total_daily_energy_expenditure(
                age=32,
                biological_sex='female',
                height=163,
                bodymass=75,
                activity_level='Sedentary',
            )
        difference_1 = abs(
            value_from_tdee_calculator_dot_net_1
            - total_daily_energy_expenditure_1
        )
        self.assertLess(difference_1, tolerance)

        # Case 2:
        value_from_tdee_calculator_dot_net_2 = 4494
        total_daily_energy_expenditure_2 = \
            calculate_total_daily_energy_expenditure(
                age=18,
                biological_sex='male',
                height=200,
                bodymass=120,
                activity_level='Athlete',
            )
        difference_2 = abs(
            value_from_tdee_calculator_dot_net_2
            - total_daily_energy_expenditure_2
        )
        self.assertLess(difference_2, tolerance)
