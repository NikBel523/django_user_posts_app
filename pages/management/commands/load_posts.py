import json
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

import MTtest.settings as settings
from pages.models import Post


User = get_user_model()


class Command(BaseCommand):
    """Команда для загрузки шаблонов постов."""

    help = 'Команда для загрузки шаблонов постов.'

    def handle(self, *args, **options):
        json_file_path = settings.BASE_DIR / 'data/posts.json'

        with open(json_file_path, 'r', encoding='utf-8') as file:
            posts_data = json.load(file)

            # Создаем список объектов Post
            posts_to_create = []
            for post_data in posts_data:
                post = Post(
                    title=post_data['title'],
                    text=post_data['text'],
                    author=User.objects.get(id=post_data['author'])
                )
                posts_to_create.append(post)

            Post.objects.bulk_create(posts_to_create)

            self.stdout.write(self.style.SUCCESS('Посты успешно загружены'))
