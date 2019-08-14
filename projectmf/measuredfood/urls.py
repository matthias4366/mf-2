from django.urls import path
from .views import (home,
                    register,
                    rawingredient,
                    rawingredient2,
                    nutrientprofile,
                    fulldayofeating,
                    mealplan
)
from django.contrib.auth import views as auth_views

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

urlpatterns_rawingredient = [
    path(
        'ingredients/create/',
        rawingredient.CreateRawIngredient.as_view(),
        name='create-raw-ingredient'
    ),
    path(
        'ingredients/list/',
        rawingredient.ListRawIngredients.as_view(),
        name='list-raw-ingredients'
    ),
    path(
        'ingredients/<int:pk>/update/',
        rawingredient.UpdateRawIngredient.as_view(),
        name='update-raw-ingredient'
    ),
    path(
        'ingredients/<int:pk>/detail/',
        rawingredient.DetailRawIngredient.as_view(),
        name='detail-raw-ingredient'
    ),
    path(
        'ingredients/<int:pk>/delete/',
        rawingredient.DeleteRawIngredient.as_view(),
        name='delete-raw-ingredient'
    ),
]

urlpatterns_rawingredient2 = [
    path(
        'rawingredient2/create/',
        rawingredient2.create_rawingredient2,
        name='create-rawingredient2'
    ),
    path(
        'rawingredient2/list/',
        rawingredient2.ListRawIngredient2.as_view(),
        name='list-rawingredient2'
    ),
    path(
        'rawingredient2/<int:pk>/update/',
        rawingredient2.UpdateRawIngredient2.as_view(),
        name='update-rawingredient2'
    ),
    path(
        'rawingredient2/<int:pk>/detail/',
        rawingredient2.DetailRawIngredient2.as_view(),
        name='detail-rawingredient2'
    ),
    path(
        'rawingredient2/<int:pk>/delete/',
        rawingredient2.DeleteRawIngredient2.as_view(),
        name='delete-rawingredient2'
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
        mealplan.CreateMealplan.as_view(),
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

urlpatterns = urlpattern_home \
+ urlpatterns_user \
+ urlpatterns_rawingredient \
+ urlpatterns_rawingredient2 \
+ urlpatterns_nutrientprofile \
+ urlpatterns_fulldayofeating \
+ urlpatterns_fulldayofeating_after_calculation \
+ urlpatterns_mealplan \
+ urlpatterns_shoppinglist
