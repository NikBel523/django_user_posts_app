from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from users.models import MetroUser

User = get_user_model()


class MetroUserView(ListView):
    """Представление для списка пользователей."""

    model = MetroUser
    template_name = 'users.html'
    context_object_name = 'users'


def user_home(request):
    """Генерация домашней страницы пользователя."""
    print(request.user)
    user = get_object_or_404(User, id=request.user.id)

    return render(
        request,
        'home.html',
        context={'profile': user},
    )
