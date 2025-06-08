from django.db import models
from django.db.models.functions import Now


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    publish = models.DateTimeField(
        db_default=Now()
    )

    def __str__(self):
        return self.title
