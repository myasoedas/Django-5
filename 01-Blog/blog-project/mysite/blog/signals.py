# blog/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector
from .models import Post


@receiver(post_save, sender=Post)
def update_search_vector(sender, instance, **kwargs):
    print(f"[SIGNAL] Обновляем search_vector для поста {instance.id}")
    Post.objects.filter(id=instance.id).update(
        search_vector=(
            SearchVector("title", weight="A", config="russian") +
            SearchVector("body", weight="B", config="russian")
        )
    )
