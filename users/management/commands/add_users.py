import json

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

import MTtest.settings as settings

User = get_user_model()


class Command(BaseCommand):
    """Команда создания тестовых суперпользователей."""

    help = 'Создаёт 3х суперпользователей.'

    def handle(self, *args, **options):
        json_file_path = settings.BASE_DIR / 'data/superusers.json'

        with open(json_file_path, 'r', encoding='utf-8') as file:
            users_data = json.load(file)

            # Создаем список объектов User
            users_to_create = []
            for user_data in users_data:
                user = User(
                    username=user_data['username'],
                    email=user_data['email'],
                    full_name=user_data['full_name'],
                    address=user_data['address'],
                    password=make_password(user_data['password']),
                    is_superuser=True,
                    is_staff=True,
                )
                users_to_create.append(user)

            User.objects.bulk_create(users_to_create)

            self.stdout.write(self.style.SUCCESS('Пользователи успешно созданы.'))
