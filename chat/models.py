from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated
from django.conf import settings


class Chat(Authored, Dated):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chat_members')
    title = models.CharField(verbose_name='chat_name', max_length=128)


class Message(Authored, Dated):
    chat = models.ForeignKey(Chat)
    message_text = models.TextField(verbose_name='message_content', max_length=255)


