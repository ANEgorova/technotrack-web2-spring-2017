from __future__ import unicode_literals

from django.db import models
from core.models import Authored, Dated


class Post(Authored, Dated):
    title = models.CharField(max_length=127)
    content = models.TextField(max_length=1000)

