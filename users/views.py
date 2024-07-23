from django.views.generic import ListView

from users.models import MetroUser


class MetroUserView(ListView):
    """Представление для списка пользователей."""

    model = MetroUser
    template_name = 'users.html'
    context_object_name = 'users'
