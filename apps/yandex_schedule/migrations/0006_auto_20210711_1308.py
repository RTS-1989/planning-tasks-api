# Generated by Django 3.1.7 on 2021-07-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_schedule', '0005_auto_20210708_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='yandex_city_code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Код города Яндекса'),
        ),
    ]
