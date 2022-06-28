# Generated by Django 4.0.2 on 2022-05-23 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0017_delete_users_alter_comment_options_and_more'),
    ]

    operations = [
        # migrations.DeleteModel(
        #     name='Users',
        # ),
        # migrations.AddField(
        #     model_name='comment',
        #     name='article',
        #     field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='articles.film'),
        # ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
