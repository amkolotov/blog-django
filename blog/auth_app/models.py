from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogUser(AbstractUser):
    email = models.EmailField(unique=True)
