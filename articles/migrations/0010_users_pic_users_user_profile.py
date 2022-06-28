# Generated by Django 4.0.2 on 2022-05-23 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0009_alter_users_options'),
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
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_from_telegram', models.IntegerField(blank=True, null=True)),
                ('full_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('pic', models.TextField(default=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
