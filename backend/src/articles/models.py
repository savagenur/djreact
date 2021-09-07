from django.db import models


class Article(models.Model):
    objects = None
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title
