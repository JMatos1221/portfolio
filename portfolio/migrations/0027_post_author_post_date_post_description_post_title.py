# Generated by Django 4.0.4 on 2022-06-05 17:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0026_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Author', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='Description', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Title', max_length=50),
        ),
    ]
