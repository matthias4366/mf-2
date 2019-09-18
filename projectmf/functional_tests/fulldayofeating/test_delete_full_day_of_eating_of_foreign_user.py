# from selenium.webdriver.support.ui import Select
# from functional_tests.utils.click_navbar_item import \
#     click_navbar_item
from ..base import FunctionalTestWithUserLoggedIn
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.common.exceptions import NoSuchElementException
# from functional_tests.utils.check_exists_by_xpath \
#     import check_exists_by_xpath
from measuredfood.models import (
    FullDayOfEating,
    NutrientProfile,
)
# from data.initial_nutrient_profiles import nutrient_profile_dict_list
from django.contrib.auth.models import User
# from data.ingredients_data2 import ingredient_dict_list
# from measuredfood.models import RawIngredient2

# import the ingredient dictionaries
import sys

sys.path.insert(0, '/projectmf/data/')


class DeleteFullDayOfEatingOfForeignUser(FunctionalTestWithUserLoggedIn):

    def test_delete_full_day_of_eating_of_foreign_user(self):
        """
        Through url forgery, a user could attempt the delete the full day
        of eating of another user. That is thwarted with the check_if_author
        function. The test is passed if the attempt to delete the foreign
        full day of eating is denied.
        """
        # Create another user.
        foreign_user = User.objects.create(
            username='Other User'
        )

        # Create a full day of eating for the foreign user. Start with the
        # nutrient profile.
        foreign_nutrientprofile = NutrientProfile.objects.create(
            name='Nutrient profile from other user',
            author=foreign_user
        )

        foreign_full_day_of_eating = FullDayOfEating.objects.create(
            name='Full day of eating from foreign user',
            author=foreign_user,
            nutrient_profile=foreign_nutrientprofile,
        )

        url_foreign_full_day_of_eating = \
            self.live_server_url \
            + '/fulldayofeating/' \
            + str(foreign_full_day_of_eating.id) \
            + '/delete/'

        # Try opening the edit page of the foreign FullDayOfEating object.
        self.browser.get(url_foreign_full_day_of_eating)

        error_message = self.browser.find_element_by_xpath(
            "//h1[1]"
        )
        error_message_text = error_message.text
        self.assertIn('403 Forbidden', error_message_text)
