from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('posts/', include('pages.urls', namespace='pages')),
    path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
]
