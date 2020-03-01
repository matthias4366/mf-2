from django.urls import path
from .views import (home,
                    register,
                    rawingredient3,
                    nutrientprofile,
                    fulldayofeating,
                    mealplan,
                    )
from django.contrib.auth import views as auth_views
from haystack.views import SearchView

urlpattern_home = [
    path('', home.home, name='home'),
    ]

urlpatterns_user = [
    path('register/', register.register, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='measuredfood/login.html'),
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

# interim code figuring out how to create html tables.
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
    path(
        'mealplan/<int:id_mealplan>/averagenutrition/',
        mealplan.mealplan_average_nutrition_view,
        name='mealplan-averagenutrition'
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
        # 'fulldayofeating/copy_fulldayofeating_to_user',
        'fulldayofeating/<int:id_fulldayofeating>/copy/',
        fulldayofeating.copy_fulldayofeating_to_user,
        name='fulldayofeating-copy-to-user',
    ),
    path(
        'fulldayofeating/search',
        SearchView(),
        name='haystack-search'
    ),
]

urlpatterns = urlpattern_home \
    + urlpatterns_user \
    + urlpatterns_rawingredient3 \
    + urlpatterns_nutrientprofile \
    + urlpatterns_fulldayofeating \
    + urlpatterns_fulldayofeating_after_calculation \
    + urlpatterns_mealplan \
    + urlpatterns_shoppinglist \
    + urlpattern_list_search
