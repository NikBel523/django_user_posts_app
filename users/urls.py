from django.urls import path
from .views import MetroUserView


app_name = 'users'

urlpatterns = [
    path('users/', MetroUserView.as_view(), name='users_list'),
]