from django.urls import path, include
from . import views
from .views import register, profile, login_view, logout_view, fav_search, favorites, add_to_favorites, remove_from_favorites, update_profile_picture
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('search/', views.subject_search, name = 'subject_search'),
    path('login/', login_view, name = 'login'),
    path('subject/<str:code>/', views.subject_detail, name = 'subject_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('profile/', profile, name = 'profile'),
    path('favorites/', favorites, name = 'favorites_page'),
    path('logout/', logout_view, name = 'logout'),
    path('fav_search/', views.fav_search, name='fav_search'),
    path('add_to_favorites/', add_to_favorites, name ="add_to_favorites"),
    path('favorites/remove/', remove_from_favorites, name="remove_from_favorites"),
    path('update-profile-picture/', update_profile_picture, name = 'update_profile_picture'),
]