import random

from .models import Category, Article


def categories(request):
    """Список категорий товаров"""
    categories = Category.objects.filter(draft=False)
    return {'categories': categories}


def reading(request):
    """Статьи, в раздел читают сейчас"""
    reading = random.sample(list(Article.objects.filter(draft=False, news=False)), k=8)
    return {'reading': reading}