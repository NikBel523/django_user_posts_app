from django.views.generic import ListView

from pages.models import Post


class PostListView(ListView):
    """Представление для списка постов."""

    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
