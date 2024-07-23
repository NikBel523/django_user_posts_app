from django.urls import path
from .views import PostListView


app_name = 'pages'

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
]