# Generated by Django 4.0.4 on 2022-06-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0042_alter_tfc_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, upload_to='contacts/'),
        ),
    ]
