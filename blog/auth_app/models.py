from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class BlogUser(AbstractUser):
    """Модель пользователя"""
    email = models.EmailField(unique=True)


class BlogUserProfile(models.Model):
    """Профиль пользователя"""
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'М'), (FEMALE, 'Ж'))

    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    gender = models.CharField('Пол', max_length=1, choices=GENDER_CHOICES, blank=True)
    obout = models.TextField('О себе', blank=True)
    date_of_birth = models.DateTimeField('Дата рождение', blank=True, null=True)
    avatar = models.ImageField('Аватар', upload_to='avatars', default='avatar/default_avatar.jpg')

    @receiver(post_save, sender=BlogUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            BlogUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=BlogUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.bloguserprofile.save()

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

    def __str__(self):
        return f'Profile - {self.user}'
