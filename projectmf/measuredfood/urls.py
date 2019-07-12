from django.urls import path
from . import old_views
from .views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home.home, name='home'),
    path('register/', old_views.register, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='measuredfood/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name='measuredfood/logout.html'
        ), name='logout'),
    path(
        'ingredients/create/',
        old_views.CreateRawIngredient.as_view(),
        name='create-raw-ingredient'
    ),
    path(
        'ingredients/list/',
        old_views.ListRawIngredients.as_view(),
        name='list-raw-ingredients'
    ),
    path(
        'ingredients/<int:pk>/update/',
        old_views.UpdateRawIngredient.as_view(),
        name='update-raw-ingredient'
    ),
    path(
        'ingredients/<int:pk>/detail/',
        old_views.DetailRawIngredient.as_view(),
        name='detail-raw-ingredient'
    ),
    path(
        'ingredients/<int:pk>/delete/',
        old_views.DeleteRawIngredient.as_view(),
        name='delete-raw-ingredient'
    ),
    # Nutrient profiles
    path(
        'nutrientprofile/create/',
        old_views.CreateNutrientProfile.as_view(),
        name='create-nutrient-profile'
    ),
    path(
        'nutrientprofile/list/',
        old_views.ListNutrientProfile.as_view(),
        name='list-nutrient-profiles'
    ),
    path(
        'nutrientprofile/<int:pk>/update/',
        old_views.UpdateNutrientProfile.as_view(),
        name='update-nutrient-profile'
    ),
    path(
        'nutrientprofile/<int:pk>/detail/',
        old_views.DetailNutrientProfile.as_view(),
        name='detail-nutrient-profile'
    ),
    path(
        'nutrientprofile/<int:pk>/delete/',
        old_views.DeleteNutrientProfile.as_view(),
        name='delete-nutrient-profile'
    ),
    # Interim recipe
    path(
        'interim_recipe/creation',
        old_views.DeleteNutrientProfile.as_view(),
        name='interim-recipe-creation'
    ),
]
