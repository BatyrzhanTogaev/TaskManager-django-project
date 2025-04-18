from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CreatedUser, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='LoginPage'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('register/', CreatedUser, name='RegisterPage'),
]
