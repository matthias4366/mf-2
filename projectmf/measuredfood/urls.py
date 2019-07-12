from django.urls import path
from .views import (home,
                    register,
                    rawingredient,
                    nutrientprofile
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home.home, name='home'),
    path('register/', register.register, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='measuredfood/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name='measuredfood/logout.html'
        ), name='logout'),
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
    # Nutrient profiles
    path(
        'nutrientprofile/create/',
        nutrientprofile.CreateNutrientProfile.as_view(),
        name='create-nutrient-profile'
    ),
    path(
        'nutrientprofile/list/',
        nutrientprofile.ListNutrientProfile.as_view(),
        name='list-nutrient-profiles'
    ),
    path(
        'nutrientprofile/<int:pk>/update/',
        nutrientprofile.UpdateNutrientProfile.as_view(),
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
    # Interim recipe
    path(
        'interim_recipe/creation',
        nutrientprofile.DeleteNutrientProfile.as_view(),
        name='interim-recipe-creation'
    ),
]
