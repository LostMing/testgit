# Generated by Django 4.0.6 on 2022-07-22 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='naver_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NEWS_TITLE', models.CharField(max_length=150)),
                ('NEWS_URL', models.URLField(unique=True)),
            ],
        ),
    ]