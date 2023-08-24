# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users', verbose_name = 'аватар', **NULLABLE)
    country = models.CharField(verbose_name='Страна', **NULLABLE)
    verification_code = models.CharField(verbose_name='код', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
