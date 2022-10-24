# Generated by Django 2.2.16 on 2022-08-11 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка на категорию')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название жанра')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка на жанр')),
            ],
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('year', models.DateTimeField(verbose_name='Дата выхода')),
                ('category', models.ForeignKey(help_text='Категория, к которой относится произведение', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='categories.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(help_text='Жанр(ы), к которому(ым) относится произведение', related_name='genre', through='categories.GenreTitle', to='categories.Genre', verbose_name='Жанр')),
            ],
        ),
        migrations.AddField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.Title'),
        ),
    ]
