from django.urls import path
from .views import MetroUserView, UserUpdateView, user_home

app_name = 'users'

urlpatterns = [
    path('', MetroUserView.as_view(), name='users_list'),
    path('home/', user_home, name='user_home'),
    path('<int:user_id>/', UserUpdateView.as_view(), name='user_update'),
]
