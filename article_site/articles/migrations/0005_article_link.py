# Generated by Django 5.0.3 on 2024-03-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_tag_article_tags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.URLField(default='https://habr.com/ru/articles/'),
        ),
    ]
