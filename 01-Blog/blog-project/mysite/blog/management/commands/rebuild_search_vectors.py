from django.core.management.base import BaseCommand
from django.contrib.postgres.search import SearchVector
from blog.models import Post


class Command(BaseCommand):
    help = "Пересчитывает поле search_vector для всех постов"

    def handle(self, *args, **kwargs):
        updated = Post.objects.update(
            search_vector=(
                SearchVector("title", weight="A", config="russian") +
                SearchVector("body", weight="B", config="russian")
            )
        )
        self.stdout.write(self.style.SUCCESS(f"Обновлено постов: {updated}"))
