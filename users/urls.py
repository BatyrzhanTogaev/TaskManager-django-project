from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import CreatedUser

urlpatterns = [
    path('login/', LoginView.as_view(), name='LoginPage'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('register/', CreatedUser, name='RegisterPage'),
]
