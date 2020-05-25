from django.urls import path
from .views import (
    home,
    register,
    login,
    rawingredient3,
    nutrientprofile,
    fulldayofeating,
    fulldayofeating2,
    mealplan,
    contact,
    onboarding_first_use,
)
from django.contrib.auth import views as auth_views
from haystack.views import SearchView

urlpattern_home = [
    path('', home.home, name='home'),
    ]

urlpattern_initial_tutorial = [
    path(
        'nutrientprofile_make_for_user/',
        onboarding_first_use.nutrientprofile_make_for_user,
        name='nutrientprofile-make-for-user'
    ),
]

urlpatterns_user = [
    path('register/', register.register, name='register'),
    path('login/',
         login.login_custom_view,
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name='measuredfood/logout.html'
                                        ), name='logout'),
]

urlpatterns_rawingredient3 = [
    path(
        'rawingredient3/create/',
        rawingredient3.create_rawingredient3,
        name='create-rawingredient3'
    ),
    path(
        'rawingredient3/list/',
        rawingredient3.ListRawIngredient3.as_view(),
        name='list-rawingredient3'
    ),
    path(
        'rawingredient3/<int:pk>/detail/',
        rawingredient3.DetailRawIngredient3.as_view(),
        name='detail-rawingredient3'
    ),
    path(
        'rawingredient3/<int:id_rawingredient3>/update/',
        rawingredient3.update_rawingredient3,
        name='update-rawingredient3'
    ),
    path(
        'rawingredient3/<int:pk>/delete/',
        rawingredient3.DeleteRawIngredient3.as_view(),
        name='delete-rawingredient3'
    ),
    path(
        'rawingredient3/get_from_food_data_central/',
        rawingredient3.get_from_food_data_central,
        name='get-from-food-data-central'
    ),
]

urlpatterns_nutrientprofile = [
    path(
        'nutrientprofile/create/',
        nutrientprofile.create_nutrientprofile,
        name='create-nutrient-profile'
    ),
    path(
        'nutrientprofile/list/',
        nutrientprofile.ListNutrientProfile.as_view(),
        name='list-nutrient-profiles'
    ),
    path(
        'nutrientprofile/<int:id_nutrientprofile>/update/',
        nutrientprofile.update_nutrientprofile,
        name='update-nutrient-profile'
    ),
    path(
        'nutrientprofile/<int:pk>/detail/',
        nutrientprofile.DetailNutrientProfile.as_view(),
        name='detail-nutrient-profile'
    ),
    path(
        'nutrientprofile/<int:pk>/delete/',
        nutrientprofile.DeleteNutrientProfile.as_view(),
        name='delete-nutrient-profile'
    ),
]

urlpatterns_fulldayofeating = [
    path(
        'fulldayofeating/create/',
        fulldayofeating.create_fulldayofeating_view,
        name='create-fulldayofeating'
    ),
    path(
        'fulldayofeating/<int:id_fulldayofeating>/update/',
        fulldayofeating.update_fulldayofeating_view,
        name='update-fulldayofeating'
         ),
    path(
        'fulldayofeating/list/',
        fulldayofeating.ListFullDayOfEating.as_view(),
        name='list-fulldayofeating'
    ),
    path(
        'fulldayofeating/<int:pk>/detail/',
        fulldayofeating.DetailFullDayOfEating.as_view(),
        name='detail-fulldayofeating'
    ),
    path(
        'fulldayofeating/<int:pk>/delete/',
        fulldayofeating.DeleteFullDayOfEating.as_view(),
        name='delete-fulldayofeating'
    ),
]

urlpatterns_fulldayofeating2 = [
    path(
        'fulldayofeating2/create/',
        fulldayofeating2.create_fulldayofeating2_view,
        name='create-fulldayofeating2'
    ),
    path(
        'fulldayofeating2/<int:id_fulldayofeating2>/update/',
        fulldayofeating2.update_fulldayofeating2_view,
        name='update-fulldayofeating2'
         ),
    path(
        'fulldayofeating2/list/',
        fulldayofeating2.ListFullDayOfEating2.as_view(),
        name='list-fulldayofeating2'
    ),
    path(
        'fulldayofeating2/<int:pk>/detail/',
        fulldayofeating2.DetailFullDayOfEating2.as_view(),
        name='detail-fulldayofeating2'
    ),
    path(
        'fulldayofeating2/<int:pk>/delete/',
        fulldayofeating2.DeleteFullDayOfEating2.as_view(),
        name='delete-fulldayofeating2'
    ),
]

urlpatterns_fulldayofeating_after_calculation = [
    path(
        'fulldayofeating/<int:id_fulldayofeating>/calculate/',
        fulldayofeating.calculate_fulldayofeating_view,
        name='calculate-fulldayofeating'
    ),
]

urlpatterns_mealplan = [
    path(
        'mealplan/create/',
        mealplan.create_mealplan_view,
        name='create-mealplan'
    ),
    path(
        'mealplan/<int:id_mealplan>/update/',
        mealplan.update_mealplan_view,
        name='update-mealplan'
         ),
    path(
        'mealplan/list/',
        mealplan.ListMealplan.as_view(),
        name='list-mealplan'
    ),
    path(
        'mealplan/<int:pk>/detail/',
        mealplan.DetailMealplan.as_view(),
        name='detail-mealplan'
    ),
    path(
        'mealplan/<int:pk>/delete/',
        mealplan.DeleteMealplan.as_view(),
        name='delete-mealplan'
    ),
]

urlpatterns_shoppinglist = [
    path(
        'mealplan/<int:id_mealplan>/shoppinglist/',
        mealplan.shoppinglist_view,
        name='mealplan-shoppinglist'
    ),
]

urlpattern_list_search = [
    path(
        'fulldayofeating/<int:id_fulldayofeating>/copy/',
        fulldayofeating.copy_fulldayofeating_to_user,
        name='fulldayofeating-copy-to-user',
    ),
    path(
        # TODO: rewrite as more general /search
        'fulldayofeating/search',
        SearchView(),
        name='haystack-search'
    ),
    path(
        'nutrientprofile/<int:id_nutrientprofile>/copy/',
        nutrientprofile.copy_nutrientprofile_to_user,
        name='nutrientprofile-copy-to-user',
    ),
    path(
        'mealplan/<int:id_mealplan>/copy/',
        mealplan.copy_mealplan_to_user,
        name='mealplan-copy-to-user',
    ),
]

urlpattern_contact = [
    path(
        'contact',
        contact.contact_view,
        name='contact'
    )
]

urlpatterns = urlpattern_home \
    + urlpattern_initial_tutorial \
    + urlpatterns_user \
    + urlpatterns_rawingredient3 \
    + urlpatterns_nutrientprofile \
    + urlpatterns_fulldayofeating \
    + urlpatterns_fulldayofeating2 \
    + urlpatterns_fulldayofeating_after_calculation \
    + urlpatterns_mealplan \
    + urlpatterns_shoppinglist \
    + urlpattern_list_search \
    + urlpattern_contact
