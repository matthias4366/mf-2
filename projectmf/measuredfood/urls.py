from django.urls import path
from .views import (home,
                    register,
                    rawingredient2,
                    nutrientprofile,
                    fulldayofeating,
                    mealplan,
                    tolerableupperintake
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
        'rawingredient2/<int:id_rawingredient2>/update/',
        rawingredient2.update_rawingredient2,
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

urlpatterns_tolerableupperintake = [
    path(
        'tolerableupperintake/create/',
        tolerableupperintake.create_tolerableupperintake_view,
        name='create-tolerableupperintake'
    ),
    path(
        'tolerableupperintake/list/',
        tolerableupperintake.ListTolerableUpperIntake.as_view(),
        name='list-tolerableupperintake'
    ),
    path(
        'tolerableupperintake/<int:id_tolerableupperintake>/update/',
        tolerableupperintake.update_tolerableupperintake_view,
        name='update-tolerableupperintake'
    ),
    path(
        'tolerableupperintake/<int:pk>/detail/',
        tolerableupperintake.DetailTolerableUpperIntake.as_view(),
        name='detail-tolerableupperintake'
    ),
    path(
        'tolerableupperintake/<int:pk>/delete/',
        tolerableupperintake.DeleteTolerableUpperIntake.as_view(),
        name='delete-tolerableupperintake'
    ),
]

urlpatterns = urlpattern_home \
+ urlpatterns_user \
+ urlpatterns_rawingredient2 \
+ urlpatterns_nutrientprofile \
+ urlpatterns_fulldayofeating \
+ urlpatterns_fulldayofeating_after_calculation \
+ urlpatterns_mealplan \
+ urlpatterns_shoppinglist \
+ urlpatterns_tolerableupperintake
