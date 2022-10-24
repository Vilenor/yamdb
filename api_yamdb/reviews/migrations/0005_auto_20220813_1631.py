# Generated by Django 2.2.16 on 2022-08-13 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20220813_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='categories.Title'),
        ),
    ]
