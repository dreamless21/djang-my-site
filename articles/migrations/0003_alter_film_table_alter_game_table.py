# Generated by Django 4.0.2 on 2022-05-20 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment_users_game_alter_film_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='film',
            table='anime',
        ),
        migrations.AlterModelTable(
            name='game',
            table='games',
        ),
    ]
