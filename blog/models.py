from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True, null=True)

