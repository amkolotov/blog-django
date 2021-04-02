import json
import os

from django.core.management import BaseCommand

from auth_app.models import BlogUser
from main_app.models import Category, Tag, Article

JSON_PATH = 'main_app/db_json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name)) as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = load_from_json('users.json')
        BlogUser.objects.all().delete()

        for user in users:
            BlogUser.objects.create(**user)

        categories = load_from_json('categories.json')
        Category.objects.all().delete()

        for category in categories:
            Category.objects.create(**category)

        tags = load_from_json('tags.json')
        Tag.objects.all().delete()

        for tag in tags:
            Tag.objects.create(**tag)

        articles = load_from_json('articles.json')
        Article.objects.all().delete()

        for article in articles:
            category_name = article['category']
            _category = Category.objects.get(name=category_name)
            article['category'] = _category

            user_name = article['author']
            _user = BlogUser.objects.get(username=user_name)
            article['author'] = _user

            art = Article.objects.create(
                title=article['title'],
                category=article['category'],
                poster=article['poster'],
                author=article['author'],
                short_desc=article['short_desc'],
                text=article['text'],
                news=article['news'],
                draft=article['draft']
            )
            for item in article['tags']:
                tag = Tag.objects.filter(name=item).first()
                art.tags.add(tag)



