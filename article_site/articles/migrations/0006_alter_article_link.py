# Generated by Django 5.0.3 on 2024-03-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.URLField(),
        ),
    ]
