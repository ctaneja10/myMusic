# Generated by Django 4.1.4 on 2023-03-02 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0006_remove_song_id_song_song_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_slug',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
