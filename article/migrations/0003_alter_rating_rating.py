# Generated by Django 5.0.1 on 2024-03-05 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10),
        ),
    ]