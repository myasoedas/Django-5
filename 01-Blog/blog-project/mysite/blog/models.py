from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex


class Post(models.Model):
    # Вложенное перечисление возможных статусов поста.
    # Используется TextChoices для строгой типизации и автокомплита в IDE.
    # Значения хранятся в БД как строки, но доступны по атрибутам (Post.Status.DRAFT).
    class Status(models.TextChoices):
        DRAFT = (
            "DF",
            "Черновик",
        )  # Пост не опубликован, доступен только в админке.
        PUBLISHED = "PB", "Опубликовано"  # Пост виден в публичной части сайта.

    # Заголовок поста, используется в списках и мета-тегах.
    title = models.CharField(
        max_length=250,
        verbose_name="Заголовок",  # Отображается в админке
        help_text="Введите заголовок поста",  # Подсказка в админке под полем
    )

    # URL-safe идентификатор. Используется в адресной строке, должен быть уникальным в рамках даты.
    slug = models.SlugField(
        max_length=250,
        verbose_name="Слаг",
        help_text="URL-идентификатор поста (только латиница, цифры, дефис)",
    )

    # Внешний ключ на модель пользователя. Один пользователь — много постов.
    # on_delete=models.CASCADE: удаление автора приведёт к удалению его постов.
    # related_name: позволяет получить все посты пользователя через user.blog_posts.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        verbose_name="Автор",
        help_text="Пользователь, написавший пост",
    )

    # Основное содержимое статьи. Хранится как текст без ограничения по длине.
    body = models.TextField(
        verbose_name="Содержимое", help_text="Основной текст статьи"
    )

    # Дата и время публикации поста. Можно задать вручную или оставить автоустановку.
    publish = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата публикации",
        help_text="Дата и время публикации",
    )

    # Дата создания поста. Устанавливается один раз автоматически при создании записи.
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Создан", help_text="Дата создания"
    )

    # Дата последнего изменения. Автоматически обновляется при каждом сохранении.
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Обновлён",
        help_text="Дата последнего изменения",
    )

    # Статус публикации (черновик / опубликован). Значение ограничено выбором из перечисления.
    status = models.CharField(
        max_length=2,
        choices=Status.choices,  # Ограничение значений на уровне модели и формы
        default=Status.DRAFT,  # Значение по умолчанию — черновик
        verbose_name="Статус",
        help_text="Текущий статус публикации",
    )
    search_vector = SearchVectorField(null=True, editable=False)

    class Meta:
        # Сортировка по дате публикации по убыванию (новые — первыми).
        ordering = ["-publish"]

        # Индекс на поле publish — улучшает производительность сортировки и фильтрации.
        indexes = [
            models.Index(fields=["-publish"]),
            GinIndex(
                name="idx_post_title_trgm",
                fields=["title"],
                opclasses=["gin_trgm_ops"],
            ),
            GinIndex(
                name="idx_post_body_trgm",
                fields=["body"],
                opclasses=["gin_trgm_ops"],
            ),
            GinIndex(fields=["search_vector"]),
        ]

        # Человекочитаемые имена модели для отображения в админке.
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    # Строковое представление модели — удобно для отображения в админке и логах.
    def __str__(self):
        return self.title
