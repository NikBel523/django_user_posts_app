from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    """Форма для изменения информации о пользователе."""

    class Meta:
        model = User
        fields = ['full_name', 'email', 'avatar', 'address']
