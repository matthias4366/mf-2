from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='measuredfood/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(
             template_name='measuredfood/logout.html'
        ), name='logout'),
    path(
        'ingredients/create/',
        views.CreateRawIngredient.as_view(),
        name='create-raw-ingredient'
    ),
    path(
        'ingredients/list/',
        views.ListRawIngredients.as_view(),
        name='list-raw-ingredients'
    ),
    path(
        'ingredients/<int:pk>/update/',
        views.UpdateRawIngredient.as_view(),
        name='update-raw-ingredient'
    ),
    path(
        'ingredients/<int:pk>/detail/',
        views.DetailRawIngredient.as_view(),
        name='detail-raw-ingredient'
    ),
    path(
        'ingredients/<int:pk>/delete/',
        views.DeleteRawIngredient.as_view(),
        name='delete-raw-ingredient'
    ),
]