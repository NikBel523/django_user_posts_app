from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from users.forms import UserForm
from users.models import MetroUser

User = get_user_model()


class MetroUserView(ListView):
    """Представление для списка пользователей."""

    model = MetroUser
    template_name = 'users.html'
    context_object_name = 'users'


class UserUpdateView(UpdateView):
    """Представление для изменения информации о пользователе."""

    model = User
    form_class = UserForm
    template_name = 'user_update_form.html'
    pk_url_kwarg = 'user_id'
    success_url = reverse_lazy('user_list')


def user_home(request):
    """Генерация домашней страницы пользователя."""
    print(request.user)
    user = get_object_or_404(User, id=request.user.id)

    return render(
        request,
        'home.html',
        context={'profile': user},
    )
