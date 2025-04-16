from django.urls import path
from .views import home_page, create_task


urlpatterns = [
    path('task/create/', create_task, name='CreateTask'),
    path('', home_page, name='HomePage'),
]
