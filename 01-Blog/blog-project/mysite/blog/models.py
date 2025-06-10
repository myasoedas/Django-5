from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'          # Код DF, человекочитаемое название — Черновик
        PUBLISHED = 'PB', 'Опубликовано'  # Код PB, человекочитаемое название — Опубликовано

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,               # Храним 2 символа (DF или PB)
        choices=Status.choices,     # Список допустимых значений из перечисления
        default=Status.DRAFT,       # Значение по умолчанию — черновик
    )

    class Meta:
        ordering = ['-publish']     # Сортировка по дате публикации (сначала новые)
        indexes = [
            models.Index(fields=['-publish']),  # Индекс для ускорения сортировки
        ]

    def __str__(self):
        return self.title
