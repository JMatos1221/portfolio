# Generated by Django 4.0.4 on 2022-06-05 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_alter_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default='projects/default.png', upload_to='projects/'),
        ),
    ]