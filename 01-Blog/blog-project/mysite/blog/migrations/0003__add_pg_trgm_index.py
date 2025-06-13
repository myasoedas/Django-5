from django.contrib.postgres.indexes import GinIndex
from django.db import migrations


dep_02 = (
    '0002_alter_post_options_alter_post_author_alter_post_body_and_more'
)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', dep_02),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=GinIndex(
                name='idx_post_title_trgm',
                fields=['title'],
                opclasses=['gin_trgm_ops'],
            ),
        ),
    ]
