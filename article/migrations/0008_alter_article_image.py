# Generated by Django 5.0.1 on 2024-03-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article/images/'),
        ),
    ]
