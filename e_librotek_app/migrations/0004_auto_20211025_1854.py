# Generated by Django 3.2.8 on 2021-10-25 23:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_librotek_app', '0003_auto_20211016_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 18, 54, 29, 552924)),
        ),
        migrations.AlterField(
            model_name='book',
            name='modificationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 18, 54, 29, 552924)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 18, 54, 29, 563470)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modificationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 18, 54, 29, 563470)),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastLogin',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 18, 54, 29, 563470), verbose_name='lastLogin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='signUp',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 18, 54, 29, 563470), verbose_name='signUp'),
        ),
    ]