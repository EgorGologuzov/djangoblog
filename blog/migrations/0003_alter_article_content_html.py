# Generated by Django 5.1.6 on 2025-03-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_image_article_avatar_article_is_visible_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content_html',
            field=models.FileField(null=True, upload_to='articles'),
        ),
    ]
