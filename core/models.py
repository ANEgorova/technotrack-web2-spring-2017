from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(verbose_name='user', upload_to='avatars', null=True)


class Authored(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class Dated(models.Model):
    created = models.DateTimeField(verbose_name='creation_time', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='update_time', auto_now=True)

    class Meta:
        abstract = True


class FriendshipRequest(Authored, Dated):
    is_confirmed = models.BooleanField(default=False)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friendship_recipient')


class Friendship(Dated):
    first = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='first_friend')
    second = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='second_friend')
