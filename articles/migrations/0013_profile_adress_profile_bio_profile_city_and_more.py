# Generated by Django 4.0.2 on 2022-05-23 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0012_users_pic_users_user_alter_profile_full_name_and_more'),
    ]

    # operations = [
    #     migrations.AddField(
    #         model_name='profile',
    #         name='adress',
    #         field=models.CharField(default=None, max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='profile',
    #         name='bio',
    #         field=models.TextField(default=None, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='profile',
    #         name='city',
    #         field=models.CharField(default=None, max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='profile',
    #         name='facebook',
    #         field=models.CharField(default=None, max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='profile',
    #         name='instagram',
    #         field=models.CharField(default=None, max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='profile',
    #         name='phone',
    #         field=models.CharField(default=None, max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='profile',
    #         name='telegram',
    #         field=models.CharField(default=None, max_length=255, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='users',
    #         name='pic',
    #         field=models.TextField(default=None),
    #     ),
    #     migrations.AddField(
    #         model_name='users',
    #         name='user',
    #         field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
    #     ),
    # ]
