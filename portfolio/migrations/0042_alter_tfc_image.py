# Generated by Django 4.0.4 on 2022-06-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0041_rename_title_new_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfc',
            name='image',
            field=models.ImageField(blank=True, upload_to='tfc/'),
        ),
    ]
