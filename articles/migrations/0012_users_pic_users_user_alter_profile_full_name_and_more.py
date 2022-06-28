# Generated by Django 4.0.2 on 2022-05-23 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0011_users_pic_users_user_alter_profile_full_name_and_more'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='users',
        #     name='pic',
        #     field=models.TextField(default=None),
        # ),
        # migrations.AddField(
        #     model_name='users',
        #     name='user',
        #     field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        # ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]