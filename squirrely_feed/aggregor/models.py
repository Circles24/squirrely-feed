from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=500)
    source = models.CharField(max_length=200)
    url = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
