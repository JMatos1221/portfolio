# Generated by Django 4.0.4 on 2022-06-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_alter_laboratory_link_alter_laboratory_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New', max_length=50)),
                ('description', models.CharField(default='Description', max_length=500)),
                ('link', models.URLField()),
            ],
        ),
    ]
