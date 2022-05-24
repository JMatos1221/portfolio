# Generated by Django 4.0.4 on 2022-05-24 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('linkedin', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='subject',
            name='ects',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='subject',
            name='lective_year',
            field=models.IntegerField(default=2019),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='subject',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
