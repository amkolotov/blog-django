from django.conf import settings
from django.db import models

from auth_app.models import BlogUser


class Category(models.Model):
    """Категории статей"""
    name = models.CharField('Категория', max_length=128)
    description = models.TextField('Описание')
    draft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Tag(models.Model):
    """Теги"""
    name = models.CharField('Тег', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):
    """Статья"""
    title = models.CharField('Статья', max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, verbose_name='Тег', blank=True)
    poster = models.ImageField('Постер', upload_to='posters/')
    short_desc = models.CharField('Описание', max_length=512)
    text = models.TextField('Текст')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    news = models.BooleanField('Новость', default=False)
    draft = models.BooleanField('Черновик', default=True)
    pub_date = models.DateTimeField('Опублткован', auto_now_add=True)
    last_edit = models.DateTimeField('Обновлен', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-pub_date']

    def get_parent_reviews(self):
        return self.reviews_set.filter(parent__isnull=True)


class Reviews(models.Model):
    """Отзывы пользователей о статье"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Родитель')
    text = models.TextField('Отзыв')

    def __str__(self):
        return f'{self.user.username} - {self.article}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
