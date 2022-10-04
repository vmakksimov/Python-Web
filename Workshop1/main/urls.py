from django.urls import path

from Workshop1.main.views import show_home, dashboard_view, profile_view, photo_view, like_pet

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('photo/details/<int:pk>/', photo_view, name='photo'),
    path('photo/like/<int:pk>/', like_pet, name='likes'),
)

