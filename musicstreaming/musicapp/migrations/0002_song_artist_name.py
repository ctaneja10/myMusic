# Generated by Django 4.1.4 on 2023-02-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist_name',
            field=models.TextField(default='artist unknown', max_length=20),
        ),
    ]
