# Generated by Django 4.0.4 on 2022-06-17 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0039_rename_title_new_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='name',
            new_name='title',
        ),
    ]