import random

from django.core.management import BaseCommand

from auth_app.models import BlogUser, BlogUserProfile
from main_app.models import Reviews, Article


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = (
            {'username': 'john', 'avatar': 'ava-1.jpeg'},
            {'username': 'alex', 'avatar': 'ava-2.jpg'},
            {'username': 'kate', 'avatar': 'ava-3.jpg'},
        )
        reviews = (
            'Хорошая статья',
            'Соответствует названию',
            'На троечку',
            'Полностью оправдала ожидания',
            'Не актуальная тема',
            'Хорошо написана'
        )

        new_users = []
        for user in users:
            old_user = BlogUser.objects.filter(username=user['username']).first()
            profile = BlogUserProfile.objects.get(user=old_user)
            profile.avatar = f'avatar/{user["avatar"]}'
            profile.save()
            new_users.append(old_user)

        articles = Article.objects.all()

        Reviews.objects.all().delete()

        for article in articles:
            random.shuffle(new_users)
            review_id = None
            for i in range(len(new_users)):
                if i % 2 == 0:
                    review = Reviews.objects.create(
                        article=article,
                        user=new_users[i],
                        text=random.choice(reviews)
                    )
                    review_id = review.id
                else:
                    Reviews.objects.create(
                        article=article,
                        user=new_users[i],
                        parent_id=review_id,
                        text=random.choice(reviews)
                    )




