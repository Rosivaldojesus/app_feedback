# Generated by Django 3.1 on 2022-04-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20220426_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='read',
            field=models.BooleanField(default=False, verbose_name='Lido?'),
        ),
    ]
