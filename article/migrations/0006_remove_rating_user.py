# Generated by Django 5.0.1 on 2024-03-05 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_rating_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
    ]
