# Generated by Django 4.0.4 on 2022-05-25 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='image.png', upload_to='portfolio/images'),
        ),
    ]
