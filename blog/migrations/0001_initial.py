# Generated by Django 5.1.6 on 2025-03-19 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.IntegerField(null=True)),
                ('create_at', models.DateTimeField()),
                ('title', models.CharField(default='[Title not set]', max_length=150)),
                ('category_list_json', models.CharField(default='[]', max_length=1000)),
                ('content_html', models.CharField(default='<p>[Content not set]</p>', max_length=10000000)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_at', models.DateTimeField()),
                ('sender_name', models.CharField(default='[Anonim]', max_length=150)),
                ('text', models.CharField(default='[Text not set]', max_length=1000)),
                ('is_visible', models.BooleanField(default=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
        ),
    ]
