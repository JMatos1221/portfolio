# Generated by Django 4.0.4 on 2022-06-17 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0031_alter_tfc_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfc',
            name='report',
            field=models.URLField(default='https://github.com', max_length=256),
        ),
    ]
